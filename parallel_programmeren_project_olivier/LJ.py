# -*- coding: utf-8 -*-

import math
import LijstVanAtomen

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

        afstand = LijstVanAtomen.afstandTussenTweeAtomen(atoomnummer=1) #1 dienst enkel om te testen

        return 4*epsilon* (math.pow(sigma/afstand,12) - math.pow(sigma/afstand,6))



