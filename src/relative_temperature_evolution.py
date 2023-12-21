#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## relative_temperature_evolution
##


from math import sqrt

def relative_evolution(period = 0, input = []):
    if (len(input) > period):
        try:
            value = round((input[-1] / input[-(1 + period)] - 1) * 100)
            return '{}'.format(value)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"
