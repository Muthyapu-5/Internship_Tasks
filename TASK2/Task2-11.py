#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:43:17 2021

@author: shivakesh
"""

T = int(input())

for i in range(T):
    a = input()
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    print(A.issubset(B))