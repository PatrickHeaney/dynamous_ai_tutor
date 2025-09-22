#!/bin/bash
source venv/bin/activate
export PYTHONPATH=$PYTHONPATH:.
python -m pytest
