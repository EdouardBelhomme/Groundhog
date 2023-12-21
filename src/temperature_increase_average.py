    #!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## temperature_increase_average
##


from math import sqrt

def increase_average(period = 0, input = []):
    if (len(input) > period):
        try:
            avg_inc = sum(list(map(lambda x, y: max(0, x - y), input[-period:], input[-(period + 1):-1]))) / period
            return '{:.2f}'.format(avg_inc)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"