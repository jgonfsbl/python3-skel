# -*- coding: utf-8 -*-
""" SKEL """

__date__ = "2022-04-25"
__author__ = "Jonathan Gonzalez"
__email__ = "j@0x30.io"


import os

from setuptools import find_packages, setup

mypackage_root_dir: str = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(mypackage_root_dir, "requirements", "master.txt")) as f:
    myrequirements: list[str] = f.read().splitlines()

with open(os.path.join(mypackage_root_dir, "README.md")) as f:
    myreadme: str = f.read()

with open(os.path.join(mypackage_root_dir, "src", "VERSION")) as f:
    myversion: str = f.read().strip()

setup(
    name="SKEL",
    description="Project SKEL(eton)",
    long_description_content_type="text/markdown",
    long_description=myreadme,
    version=myversion,
    install_requires=myrequirements,
    packages=find_packages(exclude=("docs", "events", "iac", "logs", "tests")),
    python_requires=">=3.10",
    author=__author__,
    author_email=__email__,
    license_files=("LICENSE",),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
        "Topic :: Utilities",
    ],
)
