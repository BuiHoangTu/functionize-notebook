#!/bin/bash

pandoc -f markdown -t rst README.md > README.rst
python3 setup.py sdist $1
