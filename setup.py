# SPDX-FileCopyrightText: Copyright contributors to the Software Quality Assurance as a Service (SQAaaS) project <sqaaas@ibergrid.eu>
# SPDX-FileCopyrightText: 2017-2024 Pablo Orviz <orviz@ifca.unican.es>
#
# SPDX-License-Identifier: GPL-3.0-only

import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="report2sqaaas",
    version="1.11.0",
    description="The reporting component for the SQAaaS platform",
    url="https://github.com/eosc-synergy/sqaaas-reporting",
    author="Pablo Orviz",
    author_email="orviz@ifca.unican.es",
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
    ],
    keywords="sqaaas",
    package_dir={"report2sqaaas": "report2sqaaas"},
    packages=["report2sqaaas"],
    package_data={
        "report2sqaaas": [
            "standards/SQA_baseline/QC.Acc.json",
            "standards/SQA_baseline/QC.Doc.json",
            "standards/SQA_baseline/QC.Lic.json",
            "standards/SQA_baseline/QC.Met.json",
            "standards/SQA_baseline/QC.Sec.json",
            "standards/SQA_baseline/QC.Sty.json",
            "standards/SQA_baseline/QC.Uni.json",
            "standards/SQA_baseline/QC.Ver.json",
            "standards/SQA_baseline/SvcQC.Dep.json",
            "standards/RDA_maturity_model/QC.FAIR.F.json",
            "standards/RDA_maturity_model/QC.FAIR.A.json",
            "standards/RDA_maturity_model/QC.FAIR.I.json",
            "standards/RDA_maturity_model/QC.FAIR.R.json",
        ]
    },
    # python_requires='>=3.6, <4',
    install_requires=["stevedore>=3.5.0"],
    entry_points={
        "console_scripts": [
            "report2sqaaas=report2sqaaas.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/eosc-synergy/sqaaas-reporting/issues",
        "Source": "https://github.com/eosc-synergy/sqaaas-reporting/",
    },
)
