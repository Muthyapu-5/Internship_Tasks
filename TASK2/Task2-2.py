#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:44:30 2021

@author: shivakesh
"""

M = int(input())
mset = set(map(int, input().split()))
N = int(input())
nset = set(map(int, input().split()))

mdef = mset.difference(nset)
ndef = nset.difference(mset)

output = mdef.union(ndef)

for i in sorted(list(output)):
    print(i)