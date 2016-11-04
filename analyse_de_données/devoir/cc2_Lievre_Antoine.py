#!/usr/bin/env python3
import numpy as np
params = (5, 3)
x = 10 * np.random.random(100)
y = params[0] + params[1] * x + np.random.normal(size = len(x))

def moyenne(x):
	return sum(x)/len(x)

def produit_scalaire(x, y):
	return sum([xx*yy for xx, yy in zip(x, y)])

def variance(x):
	return sum([np.square((xx - moyenne(x))) for xx in x])

def covariance(x, y):
	return sum([(xx - moyenne(x)) * (yy - moyenne(y)) for xx, yy in zip(x,y)])
	
def linear_parameter(x, y):
	return (covariance(x, y) / variance(x), moyenne(y) - (covariance(x, y) / variance(x)) * moyenne(x))
	
if __name__ == "__main__":
	params = (5, 3)
	x = 10 * np.random.random(100)
	y = params[0] + params[1] * x + np.random.normal(size = len(x))
	print(linear_parameter(x, y))
salutation_voyageur = 2
