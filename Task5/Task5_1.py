#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:44:38 2021

@author: shivakesh
"""

import re

class Main():
    def __init__(self):
        self.n = int(input())
        
        for i in range(self.n):
            self.s = input()
            print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', self.s)))
                    
if __name__ == '__main__':
    obj = Main()