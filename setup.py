#!/usr/bin/env python

try:
    from setuptools import setup
    test_extras = {
        'test_suite': 'pythonosc.test',
    }
except ImportError:
    from distutils.core import setup
    test_extras = {}


setup(
    name='python2-osc',
    version='1.4.2',
    author='mwicat',
    author_email='mwicat@gmail.com',
    description=(
        'Open Sound Control server and client implementations in pure Python'),
    long_description=open('README.rst').read(),
    url='https://github.com/mwicat/python2-osc',
    platforms='any',
    packages=[
        'pythonosc',
        'pythonosc.parsing',
        'pythonosc.test',
        'pythonosc.test.parsing',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: System :: Networking',
    ],
    **test_extras
)
