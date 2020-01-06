from setuptools import setup

setup(
    name="scrapy-mock",
    version="0.1.0",
    description="A Pytest plugin to record Scrapy responses and use them as testing fixtures.",
    url="https://github.com/tcurvelo/scrapy-mock",
    author="Thiago Curvelo",
    author_email="tcurvelo@gmail.com",
    license="MIT",
    py_modules=["scrapy_mock"],
    install_requires=[
        "pytest",
        "vcrpy",
        "scrapy"
        ],
    entry_points={"pytest11": ["nice = scrapy_mock"]},
)
