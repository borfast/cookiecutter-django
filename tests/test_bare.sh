#!/bin/sh
# this is a very simple script that tests the docker configuration for cookiecutter-django
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_bare.sh

set -o errexit
set -x

# create a cache directory
mkdir -p .cache/bare
cd .cache/bare

# create the project using the default settings in cookiecutter.json
cookiecutter ../../ --no-input --overwrite-if-exists use_docker=n "$@"
cd my_awesome_project

# Install OS deps
sudo utility/install_os_dependencies.sh install

# Install Python deps
pip install -r requirements/local.txt

# Lint by running pre-commit on all files
# Needs a git repo to find the project root
git init
git add .
pre-commit run --show-diff-on-failure -a

# run the project's tests
pytest

# Make sure the check doesn't raise any warnings
python manage.py check --fail-level WARNING

if [ -f "package.json" ]
then
    npm install
fi

# Generate the HTML for the documentation
cd docs && make html
