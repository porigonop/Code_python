#!/usr/bin/env python

from Graph import Graph
from pprint import pprint
import itertools as iter

nb_couple = 3
def in_string(string1, string2):
	"""
	define if the string2 is in the string1 2 by 2:
	F1H1H2 is in F1F2H1H2.
	"""
	#create a list af the 2by2 elt
	liste1 = []
	for elt in range(len(string1)-1):
		liste1.append(string1[elt] + string1[elt + 1])
	liste1 = liste1[::2]

	#do the same with str2
	liste2 = []
	for elt in range(len(string2)-1):
		liste2.append(string2[elt] + string2[elt + 1])
	liste2 = liste2[::2]

	#check if is in it and increment somme
	somme = 0
	for elt in liste2:
		if elt in liste1:
			somme += 1
		else:
			return False
	#check if somme is as long as str2
	if somme == len(liste2):
		return True


def valide(situation):
	"""
	define if the situation is possible or not
	"""

	for person in situation:
		with_other = False
		with_husband = False

		for other_person in situation:

			if person[0] == "F" and other_person[0] != "F":

				if person[1] != other_person[1]:
					with_other = True

				elif person[1] == other_person[1]:
					with_husband = True

		if with_other and not with_husband:
			return False
	return True


def create_graph(nb_couple, nb_island = 0):
	"""
	create the graphe from the given liste of node
	liste_node = [("H1F1", True),(...),...]
	"""

	#create all the person
	list_person = set()
	for i in range(1, nb_couple + 1):
		list_person.add("H" + str(i))
		list_person.add("F" + str(i))
	list_combinaison = set()

	#create all the situation betwen eache person on one side
	for r in range(nb_couple * 2 + 1):
		list_combinaison.add(iter.combinations(list_person, r))

	#check if the situation is correct
	valide_list = []
	for elt in list_combinaison:
		for elt1 in elt:
			if valide(elt1) and valide(list_person - set(elt1)):
				valide_list.append(elt1)

	# for each possibility, create a list of string with all the
	# possibility
	possi = []
	for possibility in range(len(valide_list)):
		possi.append("")
		for elt in valide_list[possibility]:
			possi[possibility] += elt
	liste_node =  possi
	
	print("number of node in the graph : " + \
	str(len(liste_node) * 2))
	#create the graph's node from the lisste_node
	#bark is represented by a True at the and : ("...", True/False)
	graph = Graph()
	for elt in liste_node:
		graph.add_a_node((elt, True))
		graph.add_a_node((elt, False))
	nb_edge = 0
	#create the graph's edge
	for from_node in graph.nodes:
		for to_node in graph.nodes:
			if from_node[1] and not to_node[1]:
				if from_node[0] != to_node[0]:
					if in_string(from_node[0], to_node[0]):

						if len(from_node[0]) == \
						len(to_node[0]) + 2\
							or len(from_node[0]) == \
							len(to_node[0]) + 4:
							graph.add_an_edge(from_node,\
							 to_node)
							graph.add_an_edge(to_node,\
							 from_node)
							nb_edge += 1
	
	print("number of edge : " + str(nb_edge))
	# retrieve the departure of the graph, the one with the max nb of leter
	# and with the bark
	maximum = 0
	for elt in liste_node:
		if len(elt) > maximum:
			maximum = len(elt)
			departure = elt
	departure = (departure, True)

	return graph, departure


def find_way(graph, departure, arrival):
	"""
	find a way from the depth_first_search method in the graph object
	check parent by parent from the arrival node to the departure and 
	return the way in string if there is a possibility
	return a comprenhsible strig otherwise
	"""
	parents = graph.depth_first_search(departure)
	chemin = ""
	elt = arrival
	n = 0
	while elt != departure:
		n += 1
		elt = parents[elt]
		if elt == None:
			return "no way found"
		if elt[1]:
			chemin = "B" + elt[0] + "\n" + chemin
		else:
			chemin = " " + elt[0] + "\n" + chemin
		if n == 100000:
			return "no way found under 100 000 iteration"

	return(chemin)


graph, departure = create_graph(nb_couple)
print(find_way(graph, departure, ("", False)))
