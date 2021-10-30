#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 15:48:12 2021

@author: shivakesh
"""
import numpy

N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
print(numpy.prod(numpy.sum(A, axis=0), axis=0))