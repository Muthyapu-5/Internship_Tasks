#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 16:02:34 2021

@author: shivakesh
"""

import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B), numpy.outer(A, B), sep='\n')