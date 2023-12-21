#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## switch
##


from math import sqrt

switch = 0

def switch_occurs(period, input):
    global switch
    if (len(input) > period + 1):
        try:
            value = round((input[-1] / input[-(1 + period)] - 1) * 100)
            prevalue = round((input[-2] / input[-(2 + period)] - 1) * 100)
            if (abs(prevalue + value) != abs(prevalue) + abs(value)):
                switch += 1
                return "    a switch occurs"
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return ""
    return ""