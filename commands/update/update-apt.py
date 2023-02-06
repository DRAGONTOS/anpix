#!/usr/bin/env python
#
# Imports
import os
import yaml
#
# Gets the name:
with open('config/debian.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    value = config['name']
#
# sets the install pacman command
os.system("~/.local/bin/distrobox-enter -n " + value + " -- sudo apt update && sudo apt upgrade ")
SystemExit
