from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='report2sqaaas',
    version='2.0.0',
    description='The reporting component for the SQAaaS platform',
    url='https://github.com/eosc-synergy/sqaaas-reporting',
    author='Pablo Orviz',
    author_email='orviz@ifca.unican.es',
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    ],
    keywords='sqaaas',
    package_dir={'report2sqaaas': 'report2sqaaas'},
    packages=['report2sqaaas'],
    # python_requires='>=3.6, <4',
    entry_points={
        'console_scripts': [
            'report2sqaaas=report2sqaaas.main:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/eosc-synergy/sqaaas-reporting/issues',
        'Source': 'https://github.com/eosc-synergy/sqaaas-reporting/',
    },
)
