#!/usr/bin/env bash

cd src
nohup python3 webapp_flask.py -r | tee build.out
