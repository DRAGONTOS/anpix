#!/usr/bin/env python
#
# Imports
import os
#
# What = to input
what = input('What Package Manager does your Distrobox use? ')
# Just some if statements
if what == "pacman": {
        os.system("./commands/remove/remove-pacman.py")
        }
if what == "apt": {
        os.system("./commands/remove/remove-apt.py")
        }
if what == "dnf": {
        os.system("./commands/remove/remove-dnf.py")
        }
