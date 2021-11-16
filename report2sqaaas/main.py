import argparse

from stevedore import driver, extension


def get_validators():
    mgr = extension.ExtensionManager(
        namespace="sqaaas.validators"
    )
    return dict((x.name, x.plugin) for x in mgr)


def get_parser(validators):
    parser = argparse.ArgumentParser(
        description="Run output validators for the SQAaaS-supported tools",
    )

    parser.add_argument(
        'validators',
        metavar='VALIDATOR',
        type=str,
        choices=validators,
        help=(
            'Identifier of the output validator for the tool being triggered.'
            'Allowed values: {%(choices)s}'
        )
    )

    return parser


def main():
    allowed_validators = get_validators()
    opts = get_parser(allowed_validators).parse_args()

    validator = driver.DriverManager(
        namespace="sqaaas.validators",
        name=opts.validators,
        invoke_on_load=True,
    )
    validator.driver.validate()
