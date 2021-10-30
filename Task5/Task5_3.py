#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:49:45 2021

@author: shivakesh
"""

import re

expression=r"([a-zA-Z0-9])\1+"

m = re.search(expression,input())

if m:
    print(m.group(1))
else:
    print(-1)