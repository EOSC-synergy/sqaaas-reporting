<!--
SPDX-FileCopyrightText: Copyright contributors to the Software Quality Assurance as a Service (SQAaaS) project <sqaaas@ibergrid.eu>
SPDX-FileCopyrightText: 2017-2024 Pablo Orviz <orviz@ifca.unican.es>

SPDX-License-Identifier: GPL-3.0-only
-->

# report2sqaaas
[![SQAaaS badge shields.io](https://img.shields.io/badge/sqaaas%20software-silver-lightgrey)](https://api.eu.badgr.io/public/assertions/Dzr7HNIJSv6mhaGmvb27Fg "SQAaaS silver badge achieved")
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![REUSE status](https://api.reuse.software/badge/git.fsfe.org/reuse/api)](https://api.reuse.software/info/git.fsfe.org/reuse/api)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

#### Achievements
[![SQAaaS badge](https://github.com/EOSC-synergy/SQAaaS/raw/master/badges/badges_150x116/badge_software_silver.png)](https://api.eu.badgr.io/public/assertions/Dzr7HNIJSv6mhaGmvb27Fg "SQAaaS silver badge achieved")

## Institutions owning the result
<p float="left">
     <img src="images/logo-csic.png" height="50" hspace="10"/>
     <img src="images/logo-UPV.png" height="50" hspace="10"/>
     <img src="images/logo-LIP.png" height="50" hspace="10"/>
</p>


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

## Acknowledgements
This software has been developed within the EOSC-Synergy project that has received funding from the European Union's Horizon 2020 research and innovation programme      >  \under grant agreement number 857647.

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1WF4g5KH3PnQE_Ve10QFRS-gZ0NpCQ7Qr-_km1RqnOCEF1fQt" hspace="20">
  <img src="images/logo-SYNERGY.png" height="100">
</p>
