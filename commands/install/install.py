#!/usr/bin/env python
#
# Imports
import os
#
# What = to input
what = input('What Package Manager does your Distrobox use? ')
# Just some if statements
if what == "pacman": {
        os.system("./commands/install/install-pacman.py")
        }
if what == "apt": {
        os.system("./commands/install/install-apt.py")
        }
if what == "dnf": {
        os.system("./commands/install/install-dnf.py")
        }
