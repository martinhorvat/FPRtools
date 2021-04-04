#!/usr/bin/python3

import sys
import math
import numpy as np
import zaokrozi as za

# ./napaka.py 'funkcija' 'spremenljivke (x1 x2 x3 ... xn)' 'podatki (x1 dx1 x2 dx2 ... xn dxn) v osnovnih enotah'

#----------------------------------------------------------------------------------------------------------------------------------------------------------
def klic_napaka(f, p, izpis=False, z=True):
	p = np.array(p)

	fun = f
	vre = p[:, 0]
	nap = p[:, 1]

	n = napaka(izpis, fun, vre, nap)

	vrednost = fun(*list(vre))

	if z:
		rez = za.zaok(np.array((vrednost,n)))
	else:
		rez = np.array((vrednost,n))

	if(izpis):
		print('Vrednost: ',rez[0])
		print('Absolutna napaka: ',rez[1])

	return rez

def napaka(izpis, fun, vre, nap):
	n = 0

	for i in range(len(vre)):
		if vre[i] != 0:
			o = odvod(i, fun, vre)

			n += (o * nap[i]) ** 2

	n = math.sqrt(n)

	return n

def odvod(i, fun, vre):
	dvar = np.zeros((1, len(vre)))
	dvar[0, i] = 0.001

	dvar = np.copy(vre*dvar[0])

	if dvar[i] > 0.001:
		dvar[i] = 0.001

	vred_m = fun(*list(vre-dvar))
	vred_M = fun(*list(vre+dvar))

	o = (vred_M - vred_m) / (2 * dvar[i])

	return o
#----------------------------------------------------------------------------------------------------------------------------------------------------------
	



