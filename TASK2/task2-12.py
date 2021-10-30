#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:45:45 2021

@author: shivakesh
"""

Input = set(input().split())
N = int(input())
output = True

for i in range(N):
    Input2 = set(input().split())
    if not Input2.issubset(Input):
        output = False
    if len(Input2) >= len(Input):
        output = False

print(output)