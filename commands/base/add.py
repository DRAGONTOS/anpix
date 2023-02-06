#!/usr/bin/env python
#
# Imports
import os
#
# What = to input
what = input('What Package Manager does your Distrobox use? ')
# Just some if statements
if what == "pacman": {
        os.system("./commands/base/archlinux.py")
        }
if what == "apt": {
        os.system("./commands/base/debian.py")
        }
if what == "dnf": {
        os.system("./commands/base/fedora.py")
        }
