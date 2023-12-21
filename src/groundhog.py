#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## groundhog
##


from math import sqrt
from src.temperature_increase_average import increase_average
from src.relative_temperature_evolution import relative_evolution
from src.standard_deviation import *
from src.switch import switch_occurs

switch = 0

def display_stats(pos_list, in_list, period):
    if (len(in_list) < period):
        exit(84)
    global switch
    print("Global tendency switched {} times".format(switch))
    pos_list = list(map(lambda x : abs(x - .5), pos_list))
    oth_list = sorted(pos_list)
    fin_list = oth_list[-5:]
    fin_list = list(map(lambda x : in_list[pos_list.index(x) + period - 1], fin_list))
    print("5 weirdest values are {}".format(fin_list[::-1]))

def display_results(period, input_value, input_list):
    print("g={}    r={}%    s={}{}".format(increase_average(period, input_list), relative_evolution(period, input_list), standard_deviation(period, input_list), switch_occurs(period, input_list)))

def groundhog(period):
    input_value = input()
    input_list = []
    std_dev_list = []
    mobile_avg_list = []
    pos_list = []
    while (input_value != "STOP"):
        try:
            input_list.append(float(input_value))
            display_results(period, input_value, input_list)
            std_dev_list.append(standard_deviation_n(period, input_list))
            mobile_avg_list.append(mobile_avg(period, input_list))
            std_dev_list = list(filter(None, std_dev_list))
            try:
                bande_basse = mobile_avg_list[-1] - 2 * float(std_dev_list[-1])
                bande_haute = mobile_avg_list[-1] + 2 * float(std_dev_list[-1])
                pos_list.append((input_list[-1] - bande_basse) / (bande_haute - bande_basse))
            except (IndexError, ZeroDivisionError):
                pass
        except ValueError:
            continue
        input_value = input()
        try:
            float(input_value)
        except ValueError:
            if (input_value != "STOP"):
                exit(84)
    display_stats(pos_list, input_list, period)
