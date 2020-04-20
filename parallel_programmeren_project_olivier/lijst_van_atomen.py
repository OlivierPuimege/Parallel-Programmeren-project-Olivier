# -*- coding: utf-8 -*-

"""
Module parallel_programmeren_project_olivier.lijst_van_atomen 
=================================================================

A module

"""

import numpy as np
#import math
#import scipy.constants as sc
import f2py_lijstvanatomen.lijstvanatomen as fortran


class LijstVanAtomen:
    """Dit is de klasse LijstVanAtomen, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben."""


    def __init__(self, aantal): #aantal is het aantal atomen.

        self.lijstVanAtomen = np.random.rand(aantal,3)

        print(self.lijstVanAtomen)

    def loopOverLijst(self,aantalStappen,aantalAtomen):
        """Deze functie roept de fortranfunctie op en loopt daarover"""

        n=aantalStappen     #Het aantal stappen die de simulatie neemt.
        m=aantalAtomen     #Het aantal atomen per lijst.

        print("Eerste configuratie")
        optimaleconfiguratie = LijstVanAtomen(m) #Hier wordt er een eerste configuratie gemaakt
        lengte = len(self.lijstVanAtomen)
        energie1 = fortran.f90.loopoverdelijst(optimaleconfiguratie.getLijstVanAtomen(),lengte)


        for iterator in range(n): #We itereren over het aantal stappen
            print("poging tot nieuwe configuratie")
            nieuweLijst = LijstVanAtomen(m) #een poging tot een nieuwe configuratie wordt gemaakt


            energie2 = fortran.f90.loopoverdelijst(nieuweLijst.getLijstVanAtomen(),lengte)

            if energie1>energie2:
                optimaleconfiguratie = nieuweLijst
                print("De nieuwe energie is:")
                print(energie2)
                energie1 = energie2

        return optimaleconfiguratie.getLijstVanAtomen()


    def getLijstVanAtomen(self):
        return self.lijstVanAtomen

