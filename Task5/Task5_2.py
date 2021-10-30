#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:47:12 2021

@author: shivakesh
"""

regex_pattern = r"[.,]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))