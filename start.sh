#!/bin/bash
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

FLASK_APP=run.py flask run --host=0.0.0.0 --port=8080
#python3 run.py
