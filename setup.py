#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="scrapy-mock",
    version="0.1.0",
    author="Thiago Curvelo",
    author_email="tcurvelo@gmail.com",
    maintainer="Thiago Curvelo",
    maintainer_email="tcurvelo@gmail.com",
    license="MIT",
    url="https://github.com/tcurvelo/scrapy-mock",
    description="A Pytest plugin to record Scrapy responses and use them as testing fixtures.",
    long_description=read("README.rst"),
    py_modules=["scrapy_mock"],
    python_requires=">=3.7",
    install_requires=["pytest", "requests", "Scrapy", "vcrpy"],
    classifiers=[
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["scrapy-mock = scrapy_mock"]},
)
