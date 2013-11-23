#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "mainfunction",
    version = "0.0.3",
    author = "Sean McQuillan",
    author_email = "mcquillan.sean@gmail.com",
    description = "A simple decorator for marking functions as 'main', avoiding the need for if __name__ == '__main__'",
    license = "BSD",
    keywords = "decorator mainfunction",
    url = "https://github.com/objcode/mainfunction",
    packages=['mainfunction'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        ],
    )
