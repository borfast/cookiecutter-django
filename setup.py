#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2022.08.23"

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-django",
    version=version,
    description=(
        "A Cookiecutter template for creating production-ready "
        "Django projects quickly."
    ),
    long_description=long_description,
    author="Raúl Santos",
    url="https://github.com/borfast/cookiecutter-django",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, django, "
        "skeleton, scaffolding, project directory, setup.py"
    ),
)
