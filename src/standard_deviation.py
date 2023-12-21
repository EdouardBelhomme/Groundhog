#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## standard_deviation
##


from math import sqrt

def standard_deviation(period = 0, input = []):
    if (len(input) >= period):
        try:
            avg = sum(input[-period:]) / period
            std_dev = sqrt(sum(map(lambda x:(x - avg)**2, input[-period:])) / period)
            return '{:.2f}'.format(std_dev)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def standard_deviation_n(period = 0, input = []):
    if (len(input) >= period):
        try:
            avg = sum(input[-period:]) / period
            std_dev = sqrt(sum(map(lambda x:(x - avg)**2, input[-period:])) / period)
            return '{:.2f}'.format(std_dev)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return None
    return None

def mobile_avg(period = 0, input = []):
    if (len(input) >= period):
        try:
            avg = sum(input[-period:]) / period
            std_dev = sum(input[-period:]) / period
            return std_dev
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return None
    return None