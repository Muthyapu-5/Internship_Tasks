#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:50:29 2021

@author: shivakesh
"""

import numpy

n, m = map(int, input().split())

storage = numpy.array([input().strip().split() for _ in range(n)], int)
print (storage.transpose())
print (storage.flatten())
