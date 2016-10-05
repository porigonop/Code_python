#!/usr/bin/env python3
def somme(v):
    v1 = v[:]
    if len(v) == 1:
        return v[0]
    v1[1] = v1[0] + v1[1]
    v1.pop(0)
    return somme(v1)

def moyenne(v):
    return somme(v)/len(v)

a = [3, 1, 5, 2, 4]
assert moyenne(a) == 4

