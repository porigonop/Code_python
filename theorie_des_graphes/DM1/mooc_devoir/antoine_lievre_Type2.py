#!/usr/bin/env python3

import re

def prod(liste):
    a = 1
    for elt in range(len(liste)):
        if elt % 10 == 9:
            a *= int(liste[elt])
    return a

with open("regex_sum_42.txt", "r") as fh:
    print(prod(re.findall("[0-9]+", fh.read())))

#fh = open("regex_sum_42.txt", "r")
#print(prod(re.findall("[0-9]+", fh.read())))
#fh.close()
