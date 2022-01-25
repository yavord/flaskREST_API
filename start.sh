#!/bin/sh

eval "$(conda shell.bash hook)"
conda activate "flask-env"
flask run -p 3000