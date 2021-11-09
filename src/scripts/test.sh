#!/usr/bin/env bash

set -e
set -x

pushd ../app
pytest --cov=app --cov-report=term-missing tests "${@}"
