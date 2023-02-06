#!/usr/bin/env python
#
# Imports
import os
#
# What = to input
what = input('What Package Manager does your Distrobox use? ')
# Just some if statements
if what == "pacman": {
        os.system("./commands/update/update-pacman.py")
        }
if what == "apt": {
        os.system("./commands/update/update-apt.py")
        }
if what == "dnf": {
        os.system("./commands/update/update-dnf.py")
        }
