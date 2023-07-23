# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mathsup',
    version='0.1.0',
    description='Sample package for mathsup',
    entry_points={
        'console_scripts': ['mybinary=mathsup.cli:main'],
    },
    long_description=readme,
    author='DRIOUCHE Adnane',
    url='https://github.com/Tripper98/FACTO_N.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
)
