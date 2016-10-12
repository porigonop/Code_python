#!/usr/bin/env python3
from Graph import Graph
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
		if ( value[0:2] == "= " and value[3::2].split() ==[])\
		or \
		( value[0:3] == "=! " and value[4::2].split() == []):
			self.add_an_edge(from_node, to_node, value)
		else:			
			raise NameError\
			("value doesn't fit the requirement")
		
	
	
	

