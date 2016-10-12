#!/usr/bin/env python3
from TP import FiniteStateMachine
A=FiniteStateMachine()
A.add_a_node("a")
A.add_a_node("b")
A.set_initial("a")
A.set_final("b")
A.add_a_transition("a", "b", "= s")
print(A)

def create_finite_state_machine_1():
	"""create a machine that recognize "son"
	"""
	machine = FiniteStateMachine()
	machine.add_a_node("")
	machine.add_a_node("s")
	machine.add_a_node("so")
	machine.add_a_node("son")
	
	machine.set_initial("")
	machine.set_final("son")
	
	machine.add_a_transition("", "", "!= s")
	machine.add_a_transition("", "s", "= s")
	machine.add_a_transition("s", "s", "= s")
	machine.add_a_transition("s", "so", "= o")
	machine.add_a_transition("s", "", "!= o s")
	machine.add_a_transition()
	machine.add_a_transition()
	machine.add_a_transition()
	machine.add_a_transition()
	machine.add_a_transition()
