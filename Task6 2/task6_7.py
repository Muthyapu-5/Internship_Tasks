#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:51:42 2021

@author: shivakesh
"""
import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],int)
print(numpy.max(numpy.min(storage, axis=1), axis=0))