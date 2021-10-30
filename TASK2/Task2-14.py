#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:58:33 2021

@author: shivakesh
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t));