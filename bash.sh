#!/bin/bash

export FLASK_APP=/home/debian/bonjour/bonjour.py
/usr/bin/flask run -h 10.20.60.36 -p82
