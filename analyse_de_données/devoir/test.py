#!/usr/bin/env python3
import numpy as np
def Var(X):
	a = 0
	for i in X:
		a += (i-sum(X)/len(X))**2
	return a/len(X)
	
print(Var([1,2,3]))
