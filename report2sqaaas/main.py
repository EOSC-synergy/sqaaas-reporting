import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Run parsers for SQAaaS-supported tools",
    )
    return parser


def main():
    opts = get_parser().parse_args()

    mgr = driver.DriverManager(
        namespace="report2sqaaas.parsers",
        name=opts.format,
        invoke_on_load=True,
    )
