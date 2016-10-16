#!/usr/bin/env python3

class Text:
	"""
	define the replace methode for a Text
	"""
	def __init__(self,\
	text,\
	motive,\
	replacement,\
	finite_state_machine):
		"""
		initiate the text
		text : str represent the text
		motive : str this is the motive we are looking for
		replacement : str this is the thing that 
		replace the motive
		finite_state_machine : FiniteStateMachine is the machine designed for the motive we are looking for
		"""
		self.text = text
		self.motive = motive
		self.replacement = replacement
		self.finite_state_machine = finite_state_machine
		
	def replace(self):
		"""
		allow us to replace the motive into the replacement in the text.
		"""
		positions =\
		self.finite_state_machine.look_for(self.text)
		decal = 0
		result = ""
		for pos in range(len(self.text)):
			if pos + decal in positions:
				result += self.replacement
				decal += len(self.motive) -1
			else:
				try:
					result += self.text[pos + decal]
				except:
					self.text = result
					return True
	
