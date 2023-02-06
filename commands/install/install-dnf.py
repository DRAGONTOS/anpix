#!/usr/bin/env python
#
# Imports
import os
import yaml
#
# Gets the name:
with open('config/fedora.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    value = config['name']
    smt = input('What package should be installed? ')
#
# sets the install pacman command
os.system("~/.local/bin/distrobox-enter -n " + value + " -- sudo dnf install " + smt)
SystemExit
