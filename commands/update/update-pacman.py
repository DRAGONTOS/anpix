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
#
# sets the install pacman command
os.system("~/.local/bin/distrobox-enter -n " + value + " -- sudo pacman -Syu ")
SystemExit
