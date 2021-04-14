#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="radicale-rights-acl",
    version="0.2",
    description="""
    A radicale plugin to give rights based acl list stored in property dict""",
    long_description="""
This is a radicale plugin to give users access based on a propery RADICALE:acl.
It is supposed to be a comma separated list of the patttern user:rights, e.g.:
user1:rw, user2:r, user3:rw
To use this you will probably need a radicale web plugin which can set the RDAICALE:acl property.
    """,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="GNU AGPLv3",
    install_requires=["radicale>=3"],
    author="Finn Krein",
    author_email="finn@krein.moe",
    url='https://github.com/sents/radicale-rights-acl',
    packages=["radicale_rights_acl"],)
