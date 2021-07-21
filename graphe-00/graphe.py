#!/usr/bin/env python3

# fichier : graphe.py
#  auteur : Pascal Chauvin
#    date : 2021/07/20

import random
import string


def hasard(a=1, b=100):
	return random.randint(a, b)


def poids(a=1, b=100):
	return hasard(a, b)


def nouveau_graphe(nb_sommets=4, oriente=False):
	g = dict()

	assert (nb_sommets in range(2, 26))

	sommets = list()

	for _ in range(nb_sommets):
		ok = False
		while (not ok):
			s = string.ascii_uppercase[random.randint(0, 25)]
			ok = not(s in sommets)
		sommets.append(s)

	sommets = sorted(sommets)
	print(sommets)

	for s in sommets:
		adjacents = dict()
		n = hasard(0, len(sommets) - 1)
		for i in range(n):
			ok = False
			while (not ok):
				t = sommets[hasard(0, len(sommets) - 1)]
				ok = not (s is t)
			adjacents[t] = poids()
		g[s] = adjacents

	return g


if __name__ == "__main__":
	g = nouveau_graphe()
	for v in g:
		print(v, g[v])
