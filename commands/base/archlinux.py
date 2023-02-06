#!/usr/bin/env python

import os 

name = input('What is the name of you`re distrobox? ')

with open('package-managers/archlinux.yml', 'a') as f:
    f.write('name: ' + name)
