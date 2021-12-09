import argparse
import json

from report2sqaaas import utils


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
            'Identifier of the output validator for the tool being triggered. '
            'Allowed values: {%(choices)s}'
        )
    )

    parser.add_argument(
        'input_file',
        metavar='FILE',
        type=str,
        help=(
            'Location of the file that contains the output to be validated.'
        )
    )

    for validator_name, validator in validators.items():
        group = parser.add_argument_group("%s validator plugin options" % validator_name)
        validator.populate_parser(group)

    return parser


def main():
    allowed_validators = utils.get_validators()
    opts = get_parser(allowed_validators).parse_args()

    validator = utils.get_validator(opts)
    out = validator.driver.validate(opts.input_file)
    print(json.dumps(out, indent=4))
