#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:53:15 2021

@author: shivakesh
"""

import re

Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)