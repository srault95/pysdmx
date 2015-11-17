#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_descr = ""
with open('README.rst', 'r') as fp:
	long_descr = fp.read()

setup(
	name='pysdmx',
	version='0.2.0',
    description='A python interface to SDMX',
    long_description = long_descr,
    author='Widukind team',
    author_email='dev@michaelmalter.fr',
    license = 'GPLv3',
    py_modules=['sdmx'],
	provides = ['sdmx'],
    url = 'https://github.com/widukind/pysdmx',
    install_requires=[
        'pandas',
        'lxml',
        'requests'
    ],
	test_suite = 'nose.collector',
	tests_require=[
		'nose>=1.0',
		'coverage',
		'flake8',
		'httpretty'
	],
    classifiers = [
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
         'Development Status :: 2 - Alpha',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis'
   ]
)
