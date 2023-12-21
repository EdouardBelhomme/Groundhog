#!/usr/bin/env python3

##
## EPITECH PROJECT, 2023
## B-CNA-410-BDX-4-1-groundhog-edouard.belhomme
## File description:
## main
##


from sys import argv
from src.groundhog import groundhog

def display_help():
    print("SYNOPSIS")
    print("\t./groundhog period", end='\n\n')
    print("DESCRIPTION")
    print("\tperiod\tthe number of days defining a period")

if __name__ == "__main__":
    if (len(argv) == 1 or argv[1] == '-h'):
        display_help()
    else:
        groundhog(int(argv[1]))