#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="radicale-rights-acl",
    version="0.1",
    description="""
    A radicale plugin to give rights based acl list stored in property dict""",
    long_description="""
This is a radicale plugin to give users access based on a propery RADICALE:acl.
It is supposed to be a comma separated list of the patttern user:rights, e.g.:
user1:rw, user2:r, user3:rw
There are to rights flags:
    r: read
    w: write
To use this you will need a radicale web plugin which can set the RDAICALE:acl property.
    """,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    license="GNU GPLv3",
    install_requires=["radicale"],
    author="Finn Krein",
    author_email="finn@krein.moe",
    url='https://gitlabph.physik.fu-berlin.de/fbedv/radicale/radicale-rights-acl',
    packages=["radicale_rights_acl"],)
