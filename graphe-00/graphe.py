#!/usr/bin/env python3

# fichier : graphe.py
#  auteur : Pascal Chauvin
#    date : 2021/07/21

import random
import string


def nouveau_graphe(nombre_sommets=8, nombre_aretes=6, oriente=False, alphabetique=False):
	g = dict()

	if not (nombre_sommets in range(2, 26)):
		return g

	if alphabetique:
		noms = list(string.ascii_uppercase[0:nombre_sommets])
	else:
		noms = list(string.ascii_uppercase)

	sommets = list()

	for _ in range(nombre_sommets):
		ok = False
		while (not ok):
			if alphabetique:
				s = random.choice(noms)
			else:
				s = random.choice(noms)
			ok = not(s in sommets)
		sommets.append(s)

	sommets = sorted(sommets)

	k = 0
	for s in sommets:
		g[s] = dict()
		for t in sommets:
			if k < nombre_aretes:
				if s is t:
					g[s][t] = 0 # "-"
				else:
					if oriente:
						g[s][t] = random.choice(range(1, 10))
						k += 1
					else:
						if s > t:
							g[s][t] = random.choice(range(1, 10))
							g[t][s] = g[s][t]
							k += 1
			else:
				g[s][t] = 0

	return g


def afficher_graphe(g):
	print("    ", end=" ")
	for v in g:
		print("{:>4}".format(v), end=" ")
	print()

	for v in g:
		print("{:>4}".format(v), end=" ")
		for w in g[v]:
			print("{:>4}".format(g[v][w]), end=" ")
		print()


def liste_adjacence(m):
	l = dict()
	for s in m:
		l[s] = dict()
		for t in m[s]:
			if m[s][t] != 0:
				l[s][t] = m[s][t]
	return l



if __name__ == "__main__":
	g = nouveau_graphe(6, 4, False, True)
	afficher_graphe(g)

	l = liste_adjacence(g)
	for x in l:
		print(x, l[x])


#        B    C    E    F    H    K    O    S 
#   B    0    3    3    8    1    7    5    7 
#   C    3    0    0    3    7    1    4    9 
#   E    3    0    0    9    0    6    3    1 
#   F    8    3    9    0    8    8    8    1 
#   H    1    7    0    8    0    6    4    3 
#   K    7    1    6    8    6    0    1    0 
#   O    5    4    3    8    4    1    0    1 
#   S    7    9    1    1    3    0    1    0 


#        B    C    M    N    T    X 
#   B    0    1    2    5    0    9 
#   C    5    0    6    0    6    4 
#   M    6    8    0    2    8    8 
#   N    7    9    5    0    0    8 
#   T    9    5    3    4    0    2 
#   X    5    2    2    6    1    0 


#        A    B    C    D    E    F 
#   A    0    3    4    0    9    5 
#   B    3    0    3    4    0    2 
#   C    4    3    0    6    9    7 
#   D    0    4    6    0    5    4 
#   E    9    0    9    5    0    5 
#   F    5    2    7    4    5    0 
#A {'B': 3, 'C': 4, 'E': 9, 'F': 5}
#B {'A': 3, 'C': 3, 'D': 4, 'F': 2}
#C {'A': 4, 'B': 3, 'D': 6, 'E': 9, 'F': 7}
#D {'B': 4, 'C': 6, 'E': 5, 'F': 4}
#E {'A': 9, 'C': 9, 'D': 5, 'F': 5}
#F {'A': 5, 'B': 2, 'C': 7, 'D': 4, 'E': 5}

