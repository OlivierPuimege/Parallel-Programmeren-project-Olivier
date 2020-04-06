# -*- coding: utf-8 -*-

"""
Module parallel_programmeren_project_olivier.lijst_van_atomen 
=================================================================

A module

"""

import numpy as np
import math
import scipy.constants as sc


class LijstVanAtomen:
    """Dit is de klasse atoom, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben."""


    def __init__(self, aantal): #aantal is het aantal atomen.

        self.lijstVanAtomen = np.random.rand(aantal,3)

        print(self.lijstVanAtomen)

    def afstandTussenTweeAtomen(self,atoom1,atoom2):

        x1 = self.lijstVanAtomen[atoom1,0]
        y1 = self.lijstVanAtomen[atoom1,1]
        z1 = self.lijstVanAtomen[atoom1,2]

        x2 = self.lijstVanAtomen[atoom2,0]
        y2 = self.lijstVanAtomen[atoom2,1]
        z2 = self.lijstVanAtomen[atoom2,2]
        print(math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) + math.pow((z1 - z2), 2)))

        return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) + math.pow((z1 - z2), 2))

    def pertuberen(self):

        KbT = 273*sc.Boltzmann #constante van boltzmann maal temperatuur

        for atoom1 in range(len(self.lijstVanAtomen)):
            for atoom2 in range(len(self.lijstVanAtomen)):
                if atoom1 != atoom2:
                    #Hier komt de LJpotentiaal, maar voorlopig testwaarden om te zien of dit kan werken
                    #veranderingE = LJ.LJPotentiaal(self.getAtoom(atoom1),self.getAtoom(atoom2))
                    veranderingE = 0.0#Dit is gewoon om te testen, dit wordt vervangen dor bovenstaande code als dit volledig werkt.

                    #Ik heb hier print functies gezet zodanig dat ik de loops kan testen op correctheid. Deze code moet
                    # later naar fortran of c++ want python loops zijn inneficiënt.
                    print("ze zijn niet gelijk")

                    #if np.random.rand() < math.pow(math.e, -veranderingE/KbT): #blijkbaar niet nodig, elke configuratie is ok
                        #print("Energie check succesvol!")#Blijkbaar niet nodig

                else: print("ze zijn gelijk")



    def getAtoom(self,atoomnummer):
        return self.lijstVanAtomen[atoomnummer]



#om wat te testen (afval code)
aaa = LijstVanAtomen(5)
print("test van getAtoom")
print(aaa.getAtoom(1))
aaa.pertuberen()
print("De afstand is:")
aaa.afstandTussenTweeAtomen(1,2)