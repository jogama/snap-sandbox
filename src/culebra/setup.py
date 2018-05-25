#!/usr/bin/env/ python3

from setuptools import setup, find_packages
#import semver # snap doesn't get the package; override stage? 

# for debuging
import sys
print(sys.path)

setup(
    ### Metadata
    name='cmake_py',

    ### Dependencies
    install_requires=[
        'pillow',
        'semver',
    ],

    ### Interface
    entry_points={
        'console_scripts': [
            # excecutable name = package.module:function
            'culebra = culebra.culebra:main'
        ]
    },

    ### Contents
    packages=find_packages(exclude=['test*']),
)
