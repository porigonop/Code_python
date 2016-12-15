#!/usr/bin/env python

from Graph import Graph
from pprint import pprint

def in_string(string1, string2):
	
	liste1 = []
	for elt in range(len(string1)-1):
		liste1.append(string1[elt] + string1[elt + 1])
	liste1 = liste1[::2]
	
	liste2 = []
	for elt in range(len(string2)-1):
		liste2.append(string2[elt] + string2[elt + 1])
	liste2 = liste2[::2]
	
	somme = 0
	for elt in liste2:
		if elt in liste1:
			somme += 1
		else:
			return False
	if somme == len(liste2):
		return True
	
graph = Graph()
liste_node = [
"F1F2F3F4H1H2H3H4",

"F2F3F4H1H2H3H4",
"F1F3F4H1H2H3H4",
"F1F2F4H1H2H3H4",
"F1F2F3H1H2H3H4",

"F2F3F4H2H3H4",
"F1F3F4H1H3H4",
"F1F2F4H1H2H4",
"F1F2F3H1H2H3",

"F3F4H1H2H3H4",
"F1F2H1H2H3H4",
"F1F3H1H2H3H4",
"F1F4H1H2H3H4",
"F2F4H1H2H3H4",
"F2F3H1H2H3H4",

"F3F4H3H4",
"F1F2H1H2",
"F1F3H1H2",
"F1F4H1H4",
"F2F4H2H4",
"F2F3H2H3",


"",
"F1",
"F2",
"F3",
"F4",

"F1H1",
"F2H2",
"F3H3",
"F4H4",

"F1F2",
"F3F4",
"F2F4",
"F2F3",
"F1F3",
"F1F4",

]
print(len(liste_node))
for elt in liste_node:
	graph.add_a_node((elt, True))
	graph.add_a_node((elt, False))



for from_node in graph.nodes:
	for to_node in graph.nodes:
		if from_node[1] and not to_node[1]:
			if from_node[0] != to_node[0]:
				if in_string(from_node[0], to_node[0]):
					if len(from_node[0]) == len(to_node[0]) + 2\
						or len(from_node[0]) == len(to_node[0]) + 4:
						graph.add_an_edge(from_node, to_node)
						graph.add_an_edge(to_node, from_node)
						

parents = graph.depth_first_search(("F1F2F3F4H1H2H3H4", True))
chemin = ""
elt = ("", False)
n = 0
print(graph)
pprint(parents)
while elt != ("F1F2F3F4H1H2H3H4", True):
	n += 1
	try:
		elt = parents[elt]
		if elt[1]:
			chemin = "B" + elt[0] + "\n" + chemin
		else:
			chemin = " " + elt[0] + "\n" + chemin
		if n == 100000:
			print("pas de chemin possible en 100 000 parents")
			break
	except:
		print("pas de chemin possible")
		break

print(chemin)
