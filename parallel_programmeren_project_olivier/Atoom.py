# -*- coding: utf-8 -*-


class Atoom:
#Dit is de klasse atoom, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben.

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def testfunctie(self):
        "Deze functie telt 1 op bij de waarde van x en geeft de waarde van x weer. Deze dient enkel om de klasse te testen"
        self.x += 1
        print("x = " + str(self.x))

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getz(self):
        return self.z
