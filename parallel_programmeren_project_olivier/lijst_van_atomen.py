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
import f2py_rngfortran.rngfortran as rng
from et_stopwatch import Stopwatch



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

        print("Het gemiddelde is:")
        gemiddelde = np.mean(energieLijst)
        print(gemiddelde)

        print("De standaardafwijking is:")
        standaardafwijking = np.std(energieLijst)
        print(standaardafwijking)

        return optimaleconfiguratie.getLijstVanAtomen()

    def tijdtestenRNG (self, aantalAtomen=10000, aantalConfiguraties=10000):
        stopwatchNumpy = Stopwatch()
        stopwatchNumpy.start()
        for iterator in range(aantalConfiguraties):
            numpyConfiguratie = LijstVanAtomen(aantalAtomen)
        numpyTijd = stopwatchNumpy.stop()

        print("De tijd die numpy nodig heeft is (in seconden):")
        print(numpyTijd)

        stopwatchRNG = Stopwatch()
        stopwatchRNG.start()
        x = abs(rng.rngmodule.rng(5))
        y = abs(rng.rngmodule.rng(x))
        z = abs(rng.rngmodule.rng(y))

        xlijst = np.array(x)
        ylijst = np.array(y)
        zlijst = np.array(z)
        for iterator in range(aantalConfiguraties -1):
            x = abs(rng.rngmodule.rng(z))
            xlijst = np.append(xlijst,x)

            y = abs(rng.rngmodule.rng(x))
            ylijst = np.append(ylijst, y)

            z = abs(rng.rngmodule.rng(y))
            zlijst = np.append(zlijst, z)
        rngLijst = np.vstack((xlijst,ylijst,zlijst))

        RNGtijd = stopwatchRNG.stop()

        print("De tijd die mijn RNG nodig heeft is (in seconden):")
        print(RNGtijd)


    def getLijstVanAtomen(self): #Deze functie geeft de lijst van atomen terug.
        return self.lijstVanAtomen #Dit geeft dus een lijst terug van 3 deellijsten, elk het aantal atomen groot.


zzz = LijstVanAtomen(5)

print("test van de loop")
#zzz.loopOverLijst(10,5)
print("einde loop test")
zzz.tijdtestenRNG()
