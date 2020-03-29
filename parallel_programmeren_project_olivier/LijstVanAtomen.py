# -*- coding: utf-8 -*-


import numpy as np
import math

class LijstVanAtomen:
#Dit is de klasse atoom, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben.

    #LijstVanAtomen = np.arange(0) #misschien niet nodig

    def __init__(self, aantal): #aantal is het aantal atomen.
        self.lijstVanAtomen = np.arange(0)

        for iterator in range(aantal):
            nieuwAtoom = np.random.rand(1,3)
            self.lijstVanAtomen = np.append(self.lijstVanAtomen,nieuwAtoom)
            iterator += 1

    def afstandTussenTweeAtomen(self,atoomnummer):

        x1 = self.lijstVanAtomen[atoomnummer+0]
        y1 = self.lijstVanAtomen[atoomnummer+1]
        z1 = self.lijstVanAtomen[atoomnummer+2]

        x2 = self.lijstVanAtomen[atoomnummer+3+ 0]
        y2 = self.lijstVanAtomen[atoomnummer+3+ 1]
        z2 = self.lijstVanAtomen[atoomnummer+3+ 2]

        return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) + math.pow((z1 - z2), 2))

