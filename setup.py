#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ABC Manager',
    version='0.1.0',
    description='A barebones package manager for including ABC modules into C source',
    long_description=readme,
    author='Broderick Carlin',
    author_email='Broderick.Carlin@gmail.com',
    url='https://github.com/Anti-BoilerplateCode/Manager',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

