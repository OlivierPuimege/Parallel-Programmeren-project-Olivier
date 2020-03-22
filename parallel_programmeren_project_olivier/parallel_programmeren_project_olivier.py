# -*- coding: utf-8 -*-
"""
Package parallel_programmeren_project_olivier
=======================================

A 'hello world' example.
"""
__version__ = "0.1.3"


def hello(who='world'): #Laten staan voor debug
    """'Hello world' method.

    :param str who: whom to say hello to
    :returns: a string
    """
    result = "Hello " + who
    return result

class Atoom:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
	
	def testfunctie(test):
		"Deze functie telt 1 op bij de waarde van x en geeft de waarde van x weer. Deze dient enkel om de klasse te testen"
		test.x += 1
		print("x = " + str(test.x))

testvariabele = Atoom(1,2,3)
testvariabele.testfunctie()
# eof
