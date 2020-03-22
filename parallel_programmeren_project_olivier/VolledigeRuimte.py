# -*- coding: utf-8 -*-

from Atoom import Atoom

class VolledigeRuimte:

    lijstMetAtomen = []
    #lijstMetEnergie = []

    def __init__(self, lijstMetAtomen):
        self.lijstMetAtomen = lijstMetAtomen
        #self.lijstMetEnergie = lijstMetEnergie

    def toevoegenAtoom(self, Atoom):
        self.lijstMetAtomen.append(Atoom)

    def printDeXCoordinaten(self):
        #Dit print de 'aangepaste' x-coördinaten.
        x = 0
        for i in self.lijstMetAtomen:
            self.lijstMetAtomen[x].testfunctie()
            x += 1
        #self.lijstMetAtomen.


    def LennardJonesPotentiaal(self):
        for i in lijstMetAtomen:
            for j in lijstMetAtomen:
                if i != j:
                    pass
                else:
                    lijstMetEnergie.append[5] #tijdelijke testwaarde, zal toch nog niet werken
