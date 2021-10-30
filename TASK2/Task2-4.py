#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:51:01 2021

@author: shivakesh
"""

N = int(input())

countries = set()

for i in range(N):
    countries.add(input())

print(len(countries))