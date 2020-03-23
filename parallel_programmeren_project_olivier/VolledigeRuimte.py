# -*- coding: utf-8 -*-

from Atoom import Atoom
import math

class VolledigeRuimte:

    lijstMetAtomen = []
    lijstMetEnergie = []

    def __init__(self, lijstMetAtomen, lijstMetEnergie):
        self.lijstMetAtomen = lijstMetAtomen
        self.lijstMetEnergie = lijstMetEnergie

    def toevoegenAtoom(self, Atoom):
        self.lijstMetAtomen.append(Atoom)

    def printDeXCoordinaten(self):
        #Dit print de 'aangepaste' x-coördinaten. Puur een testfunctie.
        x = 0
        for i in self.lijstMetAtomen:
            self.lijstMetAtomen[x].testfunctie()
            x += 1
        #self.lijstMetAtomen.

    def LennardJonesPotentiaal(self, Atoom1, Atoom2): #Deze functie moet misschien verhuizen als bij het optimaliseren
        x1 = Atoom1.getx()
        y1 = Atoom1.gety()
        z1 = Atoom1.getz()

        x2 = Atoom2.getx()
        y2 = Atoom2.gety()
        z2 = Atoom2.getz()

        epsilon= 1 #testwaarde =>diepte put
        sigma = 1 #Ook een testwaarde => lengte waarbij E 0 is

        afstand = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2) + math.pow((z1-z2),2))

        return 4*epsilon* (math.pow(sigma/afstand,12) - math.pow(sigma/afstand,6))



    def energieUpdaten(self):
        for i in self.lijstMetAtomen:
            for j in self.lijstMetAtomen:
                if i == j:
                    pass
                else:
                    self.lijstMetEnergie.append(self.LennardJonesPotentiaal(i,j))
