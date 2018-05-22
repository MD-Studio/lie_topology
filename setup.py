#! /usr/bin/env python
# -*- coding: utf-8 -*-

# package: lie_docking
# file: setup.py
#
# Part of ‘lie_docking’, a package providing molecular docking functionality
# for the LIEStudio package.
#
# Copyright © 2018 K.M.Visscher, VU University Amsterdam, the Netherlands
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import setup, find_packages

distribution_name = 'lie_topology'

setup(
    name=distribution_name,
    version=0.1,
    description='MDStudio component wrapping topology parsers and writers',
    author='Koen M. Visscher, VU University, Amsterdam, The Netherlands',
    author_email=['k.m.visscher@vu.nl'],
    url='https://github.com/MD-Studio/lie_topology.git',
    license='Apache Software License 2.0',
    keywords='MDStudio molecular simulation',
    platforms=['Any'],
    packages=find_packages(),
    package_data={'lie_topology': ['data/*']},
    py_modules=[distribution_name],
    install_requires=['mdstudio', 'numpy'],
    include_package_data=False,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    scripts=[],
    extras_require={
        'test': ['coverage']
    }
)