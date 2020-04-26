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

        self.lijstVanAtomen = np.random.rand(3,aantal) #Deze maakt 3 lijsten: de x-co, de y-co en de z-co

    def loopOverLijst(self,aantalStappen,aantalAtomen):
        """Deze functie roept de fortranfunctie op en loopt daarover"""

        n=aantalStappen     #Het aantal stappen die de simulatie neemt.
        m=aantalAtomen     #Het aantal atomen per lijst.

        print("Eerste configuratie")
        optimaleconfiguratie = LijstVanAtomen(m) #Hier wordt er een eerste configuratie gemaakt
        energie1 = fortran.f90.loopoverdelijst(optimaleconfiguratie.getLijstVanAtomen(),m)
        energieLijst = np.array(energie1) #Bij veel stappen wordt de lijst groot, dus neem ik een numpy list voor later het gemiddelde efficiënt te berekenen.

        for iterator in range(n): #We itereren over het aantal stappen
            print("poging tot nieuwe configuratie")
            nieuweLijst = LijstVanAtomen(m) #een poging tot een nieuwe configuratie wordt gemaakt

            energie2 = fortran.f90.loopoverdelijst(nieuweLijst.getLijstVanAtomen(),m) #de energie van de nieuwe configuratie wordt bepaald
            energieLijst =np.append(energieLijst, energie2) #De nieuwe energie wordt aan de lijst toegevoegd.

            if energie1>energie2: #A
                optimaleconfiguratie = nieuweLijst #Als de nieuwe configuratie een lagere energie heeft, wordt dat het referentiepunt.
                print("De nieuwe energie is:")
                print(energie2)
                energie1 = energie2 #Natuurlijk moet energie1 dan aangepast worden

        return optimaleconfiguratie.getLijstVanAtomen()


    def getLijstVanAtomen(self): #Deze functie geeft de lijst van atomen terug.
        return self.lijstVanAtomen #Dit geeft dus een lijst terug van 3 deellijsten, elk het aantal atomen groot.
