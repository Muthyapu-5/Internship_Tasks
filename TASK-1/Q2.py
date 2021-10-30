#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:13:15 2021

@author: shivakesh
"""
import math
import os
import random
import re
import sys



n = int(input(""))
if n%2 != 0:
    print("Weird")
elif n%2 == 0 and n in range(2,6):
    print("Not Weird")
elif n%2 == 0 and n in range(6,21):
    print("Weird")
elif n%2 == 0 and n>20:
    print("Not Weird")

