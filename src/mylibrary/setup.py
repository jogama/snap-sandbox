#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    ### Metadata
    name='mylib',
    description='toy library',

    # not testing these at the moment. 
    ### Dependencies
    # install_requires=[
    #     'strictyaml>=0.11.7',
    # ],

    # tests_require=[
    #     'nose>=1.3.7',
    #     'coverage>=4.5.1',
    # ],

    ### Contents
    packages=find_packages(exclude=['test*']),
)
