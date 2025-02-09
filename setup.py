#!/usr/bin/env python3
import os

from setuptools import find_packages, setup


def exec_file(path_segments):
    """Execute a single python file to get the variables defined in it"""
    result = {}
    code = read_file(path_segments)
    exec(code, result)
    return result


def read_file(path_segments):
    """Read a file from the package. Takes a list of strings to join to
    make the path"""
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), *path_segments)
    with open(file_path) as f:
        return f.read()


version = exec_file(("middleman", "__init__.py"))["__version__"]
long_description = read_file(("README.md",))


setup(
    name="middleman",
    version=version,
    url="https://github.com/elokapina/middleman",
    description="Matrix bot to act as a middleman ",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "commonmark>=0.9.1",
        "aiolog @ git+https://github.com/jaywink/aiolog.git@matrix-handler#egg=aiolog",
        "matrix-nio[e2e]>=0.18.0",
        "PyYAML>=5.1.2",
    ],
    extras_require={
        "postgres": ["psycopg2>=2.8.5"],
        "dev": [
            "isort==5.10.1",
            "flake8==5.0.4",
            "flake8-comprehensions==3.10.0",
            "black==22.10.0",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Allow the user to run the bot with `middleman-bot ...`
    scripts=["middleman-bot"],
)
