#!/usr/bin/env python3

# fichier : graphe.py
#  auteur : Pascal Chauvin
#    date : 2021/07/21

import random
import string


def nouveau_graphe(nombre_sommets=4, oriente=False):
	g = dict()

	if not (nombre_sommets in range(2, 26)):
		return g

	sommets = list()

	for _ in range(nombre_sommets):
		ok = False
		while (not ok):
			s = random.choice(list(string.ascii_uppercase))
			ok = not(s in sommets)
		sommets.append(s)

	sommets = sorted(sommets)

	for s in sommets:
		g[s] = dict()
		for t in sommets:
			if s is t:
				g[s][t] = 0
			else:
				g[s][t] = random.choice(range(1, 100))

	return g


def afficher_graphe(g):
	print("    ", end=" ")
	for v in g:
		print("{:>4}".format(v), end=" ")
	print()

	for v in g:
		print("{:>4}".format(v), end=" ")
		for w in g[v]:
			print("{:4}".format(g[v][w]), end=" ")
		print()


if __name__ == "__main__":
	g = nouveau_graphe()
	afficher_graphe(g)

