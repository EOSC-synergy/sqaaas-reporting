import abc
import logging
import os.path
import json
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

    def __init_subclass__(cls, **kwargs):
        required_properties = [] # NOTE disabled for the time being
        for prop in required_properties:
            if not hasattr(cls, prop):
                _reason = 'Mandatory property <%s> has not been defined!' % prop
                logger.error(_reason)
                raise NotImplementedError(_reason)
        return super().__init_subclass__(**kwargs)

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


def load_json(the_input):
    json_data = {}
    if os.path.isfile(the_input) and os.path.exists(the_input):
        logger.debug('Loading JSON: input file found: %s' % the_input)
        with open(the_input) as json_file:
            json_data = json.load(json_file)
    else:
        logger.debug('Loading JSON: input string found')
        if type(the_input) in [str]:
            json_data = json.loads(the_input)
    return json_data
