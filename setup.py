# !/usr/bin/env python3
# coding:utf-8
"""
Name       : setup.py
Author     : Kuldeep Singh Sidhu
Time       : 27-11-2020 02:58 PM
GitHub     : https://github.com/singhsidhukuldeep
Description: Used to setup and publish
"""

from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",
]

setup(
    name="request-boost",
    version="0.7",
    description="A better requests and urllib. A simple package for hitting multiple URLs and performing GET/POST requests in parallel.",
    long_description=open("README.md").read()
    + "\n\n"
    + open("CHANGELOG.md").read()
    + "\n\nRead more at https://github.com/singhsidhukuldeep/request-boost",
    long_description_content_type="text/markdown",
    url="https://github.com/singhsidhukuldeep/request-boost",
    author="Kuldeep Singh Sidhu",
    author_email="singhsidhukuldeep@gmail.com",
    classifiers=classifiers,
    keywords="request boost urllib parallel fast REST API",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
)
