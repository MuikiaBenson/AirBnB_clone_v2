#!/usr/bin/python3
""" Cleans old files"""

from fabric.api import *
import os
from datetime import datetime
import tarfile

env.hosts = ["3.84.161.176", "34.234.203.122"]
env.user = "ubuntu"


def do_clean(number=0):
    """ Removes all except given number of archives"""
    number = int(number)
    if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
