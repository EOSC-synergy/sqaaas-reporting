import abc
import logging
import os.path
import json
import re
import sys

from types import SimpleNamespace

from stevedore import driver, extension


NAMESPACE = 'sqaaas.validators'

logger = logging.getLogger('sqaaas.reporting')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class BaseValidator(abc.ABC):
    def __init__(self, opts, **kwargs):
        self.opts = opts # Make parser args (opts) available to all subclasses
        self.name = opts.validator

        init_msg = 'Running SQAaaS\' <%s> validator' % self.name
        if hasattr(self, 'threshold'):
            logger.debug(
                'Default threshold set in validator <%s> class: %s' % (
                    self.name, self.threshold
                )
            )
            try:
                if self.opts.threshold is not None:
                    logger.debug((
                        'Threshold value passed through CLI: '
                        '%s' % self.opts.threshold
                    ))
                    self.threshold = self.opts.threshold
                logger.debug(
                    'Final threshold value set for validator <%s> is '
                    '%s' % (self.name, self.threshold)
                )
            except AttributeError:
                pass
            init_msg = ' '.join([
                init_msg, '(with threshold: %s)' % self.threshold
            ])
        logger.info(init_msg)

    def __init_subclass__(cls, **kwargs):
        required_properties = [] # NOTE disabled for the time being
        for prop in required_properties:
            if not hasattr(cls, prop):
                _reason = 'Mandatory property <%s> has not been defined!' % prop
                logger.error(_reason)
                raise NotImplementedError(_reason)
        return super().__init_subclass__(**kwargs)

    def get_criterion(self):
        """
        Get the criterion associated with the given subcriterion.

        The subcriterion is passed as an input argument, and thus accessible
        through self.opts.subcriterion
        """
        criterion = None
        pattern = '(^(SvcQC|QC)\.[A-Z][a-z]{2})'
        match = re.search(pattern, self.opts.subcriterion)
        if match:
            criterion = match.group(0)
            logger.debug('Matching criterion found: %s' % criterion)
        return criterion

    @staticmethod
    def populate_parser(parser):
        pass

    @abc.abstractmethod
    def validate(self) -> dict:
        """
        Main method being called by the report2sqaaas module.

        This method shall be implemented and return at the very least a dict
        containing the value of the <valid> variable, such as:

        return {
            'valid': self.valid
        }
        """


def handle_plugin_load_error(*args):
    mgr, entry_point, exception = args
    logger.error('Cannot load validator plugin <%s>: %s' % (entry_point, exception))


def get_validators():
    mgr = extension.ExtensionManager(
        namespace=NAMESPACE,
        on_load_failure_callback=handle_plugin_load_error
    )
    validators = dict((x.name, x.plugin) for x in mgr)
    logger.debug('Found the following SQAaaS validators under namespace <%s>: %s' % (NAMESPACE, validators))
    return validators


def get_validator(opts):
    if type(opts) in [dict]:
        opts = SimpleNamespace(**opts)

    name = opts.validator
    logger.debug('Loading validator <%s> from namespace <%s>' % (name, NAMESPACE))
    return driver.DriverManager(
        namespace=NAMESPACE,
        name=name,
        invoke_on_load=True,
        invoke_args=(opts,)
    )


def load_data(the_input):
    data = {}
    is_file = False
    if os.path.isfile(the_input) and os.path.exists(the_input):
        is_file = True
        logger.debug('Input file found: %s' % the_input)
        with open(the_input) as the_file:
            data = the_file.read()
    elif type(the_input) in [str]:
        logger.debug('Input string found')
        data = the_input
    else:
        logger.error('Cannot process input data type: %s' % type(the_input))

    return data


def load_json(the_input):
    data = load_data(the_input)
    json_data = {}
    try:
        json_data = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        logger.error('Could not load JSON data: %s' % str(e))

    return json_data


def load_criterion_from_standard(criterion):
    SW_BASELINE_PATH = os.path.join(
        os.path.dirname(__file__), 'standards/SQA_baseline'
    )
    data = None
    if criterion.startswith('QC.'):
        criterion_file = os.path.join(
            SW_BASELINE_PATH, '%s.json' % criterion
        )
        logger.debug('Loading criterion <%s> from file: %s' % (
            criterion, criterion_file)
        )
        data = load_json(criterion_file)
    else:
        logger.error(
            'Criterion <%s> not found in the available standards!' % criterion
        )

    if data:
        data = data[criterion]
        logger.info('Criterion <%s> loaded successfully' % criterion)
    return data
