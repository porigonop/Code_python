#!/usr/bin/env python3
from TP import FiniteStateMachine
from Text import Text

def create_finite_state_machine_1():
	"""create a machine that recognize "son"
	"""
	machine = FiniteStateMachine()
	
	#creating node
	machine.add_a_node("")
	machine.add_a_node("s")
	machine.add_a_node("so")
	machine.add_a_node("son")
	
	#set initial and final
	machine.set_initial("")
	machine.set_final("son")
	
	#creating all the transition
	machine.add_a_transition("", "s", "= s")
	machine.add_a_transition("s", "s", "= s")
	machine.add_a_transition("s", "so", "= o")
	machine.add_a_transition("so", "s", "= s")
	machine.add_a_transition("so" , "son", "= n")
	machine.add_a_transition("son", "son", "")
	return machine
	
def create_finite_state_machine_2():
	"""
	create a machine that recognize maman
	"""
	machine = FiniteStateMachine()	
	
	#creating the node
	machine.add_a_node("")
	machine.add_a_node("m")
	machine.add_a_node("ma")
	machine.add_a_node("mam")
	machine.add_a_node("mama")
	machine.add_a_node("maman")
	
	#set initial and final
	machine.set_initial("")
	machine.set_final("maman")
	
	#creating the simple transition
	machine.add_a_transition("", "m", "= m")
	machine.add_a_transition("m", "ma", "= a")
	machine.add_a_transition("ma", "mam", "= m")
	machine.add_a_transition("mam", "mama", "= a")
	machine.add_a_transition("mama", "maman", "= n")
	
	#creating the hard transition
	machine.add_a_transition("mam", "m", "= m")
	machine.add_a_transition("mama", "mam", "= m")
	machine.add_a_transition("m", "m", "= m")
	
	return machine
	
def create_finite_state_machine(motive):
	"""
	create a machine that recognize the "motive" given as argument
	"""
	#variable initate
	temp = ""
	equal = "= "
	machine = FiniteStateMachine()
	
	#set initial : ""
	machine.add_a_node(temp)
	machine.set_initial(temp)
	
	#create the nodes for ex : "m", "ma", "mam", "mama", "maman"
	for letter in motive:
		temp += letter
		machine.add_a_node(temp)
		
	#set final : "maman"
	machine.set_final(temp)
	
	#create the "normal" transition like m -= a-> ma
	for pos in range(len(motive)):
		if motive[:pos+1] != machine.final:
			machine.add_a_transition(motive[:pos],\
			motive[:pos+1],\
			equal + motive[pos])
		else:
			machine.add_a_transition(motive[:pos],motive[:],equal+motive[-1])
			break
	
	#create the difficult transition like mama -= m-> mam 
	liste = list(machine.nodes)
	liste.sort()
	edges = list(machine.edges)
	for pos in range(len(liste)):
		for node in liste[-pos::-1]:
			for posi in range(len(node)):
				for letter in motive:
					if liste[-pos][posi:] + letter == node \
					and (liste[-pos], node, equal + letter) \
					not in machine.edges:
						temp = True
						for edge in edges:
							if letter == edge[2]:
								temp = False
						if temp:	
							machine.add_a_transition(liste[-pos], \
																				node, \
																				equal + letter)
	
	# create the return transition, like mam -= m-> m or m-= m-> m
	edges = list(machine.edges)
	for node in machine.nodes:
		
		#if there is no link from the node with the first letter 
		#of the motive we make a transition to the first letter
		if 	[item for item in edges\
								if (item[0] == node and\
										item[2][2] == motive[0])\
				] \
				== []:
			machine.add_a_transition(node, motive[0], equal + motive[0])

						
					
	return machine

#note : we can't search a motive with one or less character
texte = input("text :")
motive = input("motive :")
replacement = input("replacement :")
machine = create_finite_state_machine_2()
text = Text(texte, motive, replacement, machine)
text.replace()
print(text.text)


