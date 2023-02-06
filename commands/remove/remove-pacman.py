#!/usr/bin/env python
#
# Imports
import os
import yaml
#
# Gets the name:
with open('config/archlinux.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    value = config['name']
    smt = input('What package should be removed? ')
#
# sets the install pacman command
os.system("~/.local/bin/distrobox-enter -n " + value + " -- sudo pacman -R " + smt)
SystemExit
