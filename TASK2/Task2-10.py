#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:20:36 2021

@author: shivakesh
"""

len_set = int(input())

storage = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation = input().split()
    if operation[0] == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        storage.intersection_update(temp_storage)
    elif operation[0] == 'update':
        temp_storage = set(map(int, input().split()))
        storage.update(temp_storage)
    elif operation[0] == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        storage.symmetric_difference_update(temp_storage)
    elif operation[0] == 'difference_update':
        temp_storage = set(map(int, input().split()))
        storage.difference_update(temp_storage)
    else :
        assert False

print(sum(storage))