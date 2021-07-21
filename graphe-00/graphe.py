#!/usr/bin/env python3

# fichier : graphe.py
#  auteur : Pascal Chauvin
#    date : 2021/07/21

import random
import string


def matrice_adj(n_sommets=8, n_aretes=6, alpha=True, oriente=False):
	""" Construire aléatoirement un graphe par sa matrice d'adjacence. """
	m = dict()

	ok = (n_sommets in range(2, 26 + 1)) # au moins deux sommets

	if ok:
		ok = (n_aretes in range(n_sommets*(n_sommets - 1) // 2 + 1))

	if not ok:
		return m # matrice rendue vide si erreur

	if alpha:
		noms = list(string.ascii_uppercase[0:n_sommets])
	else:
		noms = list(string.ascii_uppercase)

	sommets = list()

	for _ in range(n_sommets):
		ok = False
		while (not ok):
			s = random.choice(noms)
			ok = not(s in sommets)
		sommets.append(s)

	sommets = sorted(sommets)

	for s in sommets:
		m[s] = dict()
		for t in sommets:
			m[s][t] = 0

	for n in range(n_aretes):
		a = random.choice(sommets)
		ok = False
		while (not ok):
			b = random.choice(sommets)
			ok = (a != b) and (m[a][b] == 0)
		m[a][b] = random.randint(1, 10)
		if (not oriente):
			m[b][a] = m[a][b]

	return m


def liste_adj(m):
	""" Construire la liste d'adjacence d'un graphe à partir de sa matrice 
	    d'adjacence. """
	l = dict()
	for s in m:
		l[s] = dict()
		for t in m[s]:
			if m[s][t] != 0:
				l[s][t] = m[s][t]
	return l


def afficher_graphe(m):
	""" Afficher un graphe donné par sa matrice d'adjacence. """
	print("    ", end=" ")
	for v in m:
		print("{:>4}".format(v), end=" ")
	print()

	for v in m:
		print("{:>4}".format(v), end=" ")
		for w in m[v]:
			print("{:>4}".format(m[v][w]), end=" ")
		print()



if __name__ == "__main__":
	m = matrice_adj(6, 8) # premières lettres de l'alphabet, non orienté

	print("--- matrice d'adjacence ---")
	afficher_graphe(m)

	print("--- liste d'adjacence ---")
	l = liste_adj(m)
	for x in l:
		print(x, l[x])

