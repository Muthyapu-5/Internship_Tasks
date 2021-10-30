#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:01:52 2021

@author: shivakesh
"""
N1 = int(input())
input1 = set(input().split());

N2 = int(input())
input2 = set(input().split());

Input = input1.intersection(input2)

print(len(Input))