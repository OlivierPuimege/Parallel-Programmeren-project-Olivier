# -*- coding: utf-8 -*-

import math

class LJ:

   

    def LJPotentiaal(self, Atoom1, Atoom2): 
        x1 = Atoom1.getx()
        y1 = Atoom1.gety()
        z1 = Atoom1.getz()

        x2 = Atoom2.getx()
        y2 = Atoom2.gety()
        z2 = Atoom2.getz()

        epsilon= 1 #testwaarde =>diepte put
        sigma = 1 #Ook een testwaarde => lengte waarbij E=0 (denk ik)

        afstand = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2) + math.pow((z1-z2),2))

        return 4*epsilon* (math.pow(sigma/afstand,12) - math.pow(sigma/afstand,6))




