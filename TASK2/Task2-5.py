#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:51:22 2021

@author: shivakesh
"""

n = int(input())
s = set(map(int, input().split()))

num = int(input())
for i in range(num):
    ip = input().split()
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))