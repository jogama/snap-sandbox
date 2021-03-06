#!/usr/bin/env/ python3

from setuptools import setup, find_packages

setup(
    ### Metadata
    name='hello_es',

    ### Dependencies
    install_requires=[
        'mylib',
    ],

    ### Interface
    entry_points={
        'console_scripts': [
            # excecutable name = package.module:function
            'hello_es = hello.hello:main'
        ]
    },

    ### Contents
    packages=find_packages(exclude=['test*']),
)
