#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:34:26 2021

@author: shivakesh
"""
import re

N = int(input())

for i in range(N):
    number = input()
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")