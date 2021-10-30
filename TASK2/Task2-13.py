#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 14:56:18 2021

@author: shivakesh
"""

if __name__ == '__main__':
    N = int(input())
    Output = [];
    for i in range(0,N):
        Input = input().split();
        if Input[0] == "print":
            print(Output)
        elif Input[0] == "insert":
            Output.insert(int(Input[1]),int(Input[2]))
        elif Input[0] == "remove":
            Output.remove(int(Input[1]))
        elif Input[0] == "pop":
            Output.pop();
        elif Input[0] == "append":
            Output.append(int(Input[1]))
        elif Input[0] == "sort":
            Output.sort();
        else:
            Output.reverse();