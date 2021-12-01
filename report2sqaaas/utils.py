import abc
import logging
import os.path
import json

from stevedore import driver, extension


NAMESPACE = 'sqaaas.validators'

logger = logging.getLogger('sqaaas.reporting')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class BaseValidator(abc.ABC):
    def __init_subclass__(cls, **kwargs):
        required_properties = ['name']
        for prop in required_properties:
            if not hasattr(cls, prop):
                raise NotImplementedError('ERROR: mandatory property <%s> has not been defined!' % prop)
        return super().__init_subclass__(**kwargs)

    def validate(self) -> dict:
        return NotImplementedError


def get_validators():
    mgr = extension.ExtensionManager(
        namespace=NAMESPACE
    )
    validators = dict((x.name, x.plugin) for x in mgr)
    logger.debug('Found the following SQAaaS validators under namespace <%s>: %s' % (NAMESPACE, validators))
    return validators


def get_validator(name):
    logger.debug('Loading validator <%s> from namespace <%s>' % (NAMESPACE, name))
    return driver.DriverManager(
        namespace=NAMESPACE,
        name=name,
        invoke_on_load=True,
    )


def load_json(the_input):
    json_data = {}
    if os.path.isfile(the_input) and os.path.exists(the_input):
        logger.debug('Loading JSON: input file found: %s' % the_input)
        with open(file_name) as json_file:
            json_data = json.load(the_input)
    else:
        logger.debug('Loading JSON: input string found')
        if type(the_input) in [str]:
            json_data = json.loads(the_input)
    return json_data
