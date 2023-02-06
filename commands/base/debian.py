#!/usr/bin/env python

import os 
name = input('what is the name of you`re distrobox? ')

with open('package-managers/debian.yml', 'a') as f:
    f.write('name: ' + name)
