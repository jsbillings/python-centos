#!/usr/bin/python -tt

from setuptools import find_packages, setup

setup(
    name="centos",
    description="Client-side modules for CentOS Services",
    author="Brian Stinson",
    author_email="centos-devel@centos.org",
    packages = find_packages(),
    license = 'MIT License',
    version = '0.0.1',
)
