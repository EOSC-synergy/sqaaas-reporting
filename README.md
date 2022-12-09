# report2sqaaas
[![SQAaaS badge shields.io](https://img.shields.io/badge/sqaaas%20software-silver-lightgrey)](https://api.eu.badgr.io/public/assertions/Dzr7HNIJSv6mhaGmvb27Fg "SQAaaS silver badge achieved")

#### Achievements 
[![SQAaaS badge](https://github.com/EOSC-synergy/SQAaaS/raw/master/badges/badges_150x116/badge_software_silver.png)](https://api.eu.badgr.io/public/assertions/Dzr7HNIJSv6mhaGmvb27Fg "SQAaaS silver badge achieved")


The reporting tool for the SQAaaS platform.

## Motivation
The [SQAaaS platform](https://github.com/eosc-synergy/SQAaaS) provides a
module for software (and services) quality assessment, which relies on the
validation of a series of checks in order to provide the final certification.
This validation is done by parsing the outputs of the tools involved in those
checks, which is carried out by the `report2sqaaas` component.

## Implementation
The `report2sqaaas` uses [stevedore](https://github.com/openstack/stevedore)
Python module to load dynamically the set of validators that are then called
by the [SQAaaS API](https://github.com/eosc-synergy/sqaaas-api-server). This
module will load all the plugins found under `sqaaas.validators` namespace.

The `report2sqaaas` can be used as a Python module, but also provides a CLI
that can facilitate the testing of the
[supported plugins](https://github.com/eosc-synergy/sqaaas-reporting-plugins).

## Installation
```
$ pip install git+https://github.com/eosc-synergy/sqaaas-reporting
```

## Usage
```
$ report2sqaaas <plugin-name> <input-file-or-string>
```

such as:
```
$ licensee detect . --json > licensee_data.json
$ report2sqaaas licensee licensee_data.json
```

## Related repositories
- [sqaaas-reporting-plugins](https://github.com/eosc-synergy/sqaaas-reporting-plugins),
  which hosts the current set of supported output validation plugins.
- [sqaaas-reporting-cookiecutter](https://github.com/eosc-synergy/sqaaas-reporting-cookiecutter),
  which provides a template to easily create the structure of new plugins.
