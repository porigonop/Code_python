#!/usr/bin/env python3
from Complex import *
a = Complex(3, 4)
b = Complex(5, 10)
c = a.multiplicate_by(b)
d = a.multiplicate_by(-3)
e = a.divide_by(b)
h = a.divide_by(-2)
f = a.sum_by(-2)
g = a.sum_by(b)

print("a :", a)
print("b :", b)
print("a * b :", c)
print("a * -3", d)
print("a / b", e)
print("a / -2", h)
print(" a + -2", f)
print("a + b", g)

print("===============")

a = complex(3, 4)
b = complex(5, 10)
c = a*b
d = a*-3
e = a/b
h = a/-2
f = a+-2
g = a+b
print("a :", a)
print("b :", b)
print("a * b :", c)
print("a * -3 :", d)
print("a / b :", e)
print("a / -2 :", h)
print(" a + -2 :", f)
print("a + b :", g)
