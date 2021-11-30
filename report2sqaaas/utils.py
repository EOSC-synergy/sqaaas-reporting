import os.path
import json

from stevedore import driver, extension


NAMESPACE = 'sqaaas.validators'


class BaseValidator(object):
    def validate(self) -> dict:
        return NotImplementedError


def get_validators():
    mgr = extension.ExtensionManager(
        namespace=NAMESPACE
    )
    return dict((x.name, x.plugin) for x in mgr)


def get_validator(name):
    return driver.DriverManager(
        namespace=NAMESPACE,
        name=name,
        invoke_on_load=True,
    )


def load_json(the_input):
    json_data = {}
    if os.path.isfile(the_input) and os.path.exists(the_input):
        with open(file_name) as json_file:
            json_data = json.load(the_input)
    else:
        if type(the_input) in [str]:
            json_data = json.loads(the_input)
    return json_data
