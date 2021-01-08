#! /usr/bin/env python

import time
from os import environ

while True:
    print("{0} = {1}".format('svc2:: TEST_ENV_VAR1', environ.get('TEST_ENV_VAR1')))
    print("{0} = {1}".format('svc2:: TEST_ENV_VAR2', environ.get('TEST_ENV_VAR2')))
    print("\n\n")
    time.sleep(4)
