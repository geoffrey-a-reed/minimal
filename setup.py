# -*- coding: utf-8 -*-

'''A setuptools-based setup module.

See https://packaging.python.org/distributing/

See:
https://pypi.python.org/pypi?%3Aaction=list_classifiers
... for list of trove classifiers

'''


from codecs import open
from os import path
from setuptools import setup, find_packages


# See https://github.com/pypa/sampleproject/setup.py
root = path.abspath(path.dirname(__file__))

with open(path.join(root, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(root, 'LICENSE.txt'), encoding='utf-8') as f:
    license = f.read()

with open(path.join(root, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read().strip()



setup(
    name='minimal',
    # See https://packaging.python.org/single_source_version/
    version=version,
    description='A minimal Python package',
    long_description=long_description,
    url='https://github.com/geoffrey-a-reed/minimal',
    author='Geoffrey A. Reed',
    author_email='geoffrey.a.reed@gmail.com',
    license=license,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='sample setuptools development',
    packages=find_packages(exclude=['test_*', 'docs']),
    extras_require={
        '': ['pytest'],
    },
    package_data={
        '': ['VERSION.txt', 'LICENSE.txt']
    },
)