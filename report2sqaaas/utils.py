from stevedore import driver, extension


NAMESPACE = 'sqaaas.validators'


class BaseValidator(object):
    def validate(self):
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
