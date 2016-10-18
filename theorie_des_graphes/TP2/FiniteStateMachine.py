#!/usr/bin/env python3
from Graph import Graph
#note : I set the lenght of the tab to 2 cause of some hard condition
# in the code, it allow to see all the code.
class FiniteStateMachine(Graph):
	
	def __init__(self):
		"""
		init the Machine with her attribute and the one from 
		Graph
		"""
		Graph.__init__(self)
		self.initial = None
		self.final = None
		self.position = None
	
	def set_initial(self, node):
		"""
		attribute the initial value of initial and position
		if node is in the "Grah" Machine, else NameError
		"""
		if node not in self.nodes:
			raise NameError("node aren't in the automate")
			return False
		
		self.initial = node
		self.position = node
		
	def set_final(self, node):
		"""
		attribute the initial value of final if node is in
		"Graph" machine, else return NameError
		"""
		if node not in self.nodes:
			raise NameError("node aren't in the automate")
			return False
		self.final = node
	
	def add_a_transition(self, from_node, to_node, value):
		"""
		allow the user to add a transition, that is the same
		as creating an edges between 2 node with a value who
		begin with '=' or '!=', a space and a list of character
		"""
		if \
		( value[0:3] == "!= " and value[4::2].split() == [] )\
		or \
		( value[0:2] == "= " and value[1::2].split() == [])\
		or \
		( value == "" ):
			self.add_an_edge(from_node, to_node, value)
		else:			
			raise NameError\
			("value doesn't fit the requirement")
			
	def move(self, letter):
		"""
		perform a move in the machine
		letter is the new character read by the program
		"""

		
		for edge in self.edges:
			if (edge[0] == self.position) and (edge[2][0:2] == "= "):
				for lettre in edge[2][2::2]:
					if lettre == letter:
						self.position = edge[1]
						if self.position == self.final:
							self.position = self.initial
							return True
							
						else:
							return None
		self.position = self.initial
		return False
	def look_for(self, text):
		"""
		return a list of position in the text where the
		automate found the motive
		"""
		result = list()
		decal = len(self.final) - 1
		for pos in range(len(text)):
			if self.move(text[pos]) == True:
				result.append(pos - decal)	
		return result
	

