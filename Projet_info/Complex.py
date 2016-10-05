#!/usr/bin/env python3
class Complex:
	""" this class represent the complex number
	"""
	def __init__(self, Re, Im):
		"""the numer is initiate with a string as "3+5i"
		"""
		try:
			self.Re = float(Re)
			self.Im = float(Im)
		except:
			raise TypeError("please enter a correct number")
			
	def __str__(self):
		""" allow the user to print the complex number
		"""
		if self.Im < 0:
			return str(self.Re) + str(self.Im) + "i"
		return str(self.Re) + "+" + str(self.Im) + "i"
		
	def multiplicate_by(self, number):
		"""allow the multiplication
		"""
		answerRE = 0
		answerIm = 0
		if type(number) is Complex:
			Re = self.Re
			answerRe = Re * number.Re -\
			self.Im * number.Im
			answerIm = Re * number.Im +\
			self.Im * number.Re
		else:
			try:
				number = float(number)
			except:
				raise TypeError("please enter a valid number")
			answerRe = self.Re * number
			answerIm = self.Im * number
		return Complex(answerRe, answerIm)
	
	def divide_by(self, number):
		"""allow the division
		"""
		answerRE = 0
		answerIm = 0
		if type(number) is Complex:
			numerator = self.multiplicate_by(Complex(number.Re, - number.Im))
			answerRe = numerator.divide_by(number.Re **2 + number.Im **2).Re
			answerIm = numerator.divide_by(number.Re **2 + number.Im **2).Im
			
		else:
			try:
				number = float(number)
			except:
				raise TypeError("please enter a valid number")
			answerRe = self.Re / number
			answerIm = self.Im / number
		return Complex(answerRe, answerIm)
			
	def sum_by(self, number):
		"""allow addition and subtraction
		"""
		answerRe = 0
		answerIm = 0
		if type(number) is Complex:
			answerRe = self.Re + number.Re
			answerIm = self.Im + number.Im
			
		else:
			try:
				number = float(number)
			except:
				raise TypeError("please enter a valid number")
			answerRe = self.Re + number
			answerIm = self.Im
		return Complex(answerRe, answerIm)
			
