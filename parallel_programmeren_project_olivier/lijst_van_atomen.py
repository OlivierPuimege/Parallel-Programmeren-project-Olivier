# -*- coding: utf-8 -*-

"""
Module parallel_programmeren_project_olivier.lijst_van_atomen 
=================================================================

A module

"""

import numpy as np
#import scipy.constants as sc
import f2py_lijstvanatomen.lijstvanatomen as fortran
import f2py_rngfortran.rngfortran as rng
from et_stopwatch import Stopwatch


class LijstVanAtomen:
    """Dit is de klasse LijstVanAtomen, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben."""


    def __init__(self, aantal): #aantal is het aantal atomen.

        self.lijstVanAtomen = np.random.rand(3*aantal) #Deze maakt 3 lijsten: de x-co, de y-co en de z-co

    def loopOverLijst(self,aantalStappen=10000,aantalAtomen=100):
        """Deze functie roept de fortranfunctie op en loopt daarover"""

      

        n=aantalStappen     #Het aantal stappen die de simulatie neemt.
        m=aantalAtomen     #Het aantal atomen per lijst.

        


        print("Eerste configuratie") #Hierna wordt respectievelijke de stopwatch aangemaakt en gestart
        stopwatch = Stopwatch()
        stopwatch.start()
        optimaleconfiguratie = LijstVanAtomen(m) #Hier wordt er een eerste configuratie gemaakt
        energie1 = fortran.f90.loopoverdelijst(optimaleconfiguratie.getLijstVanAtomen(),m)

        energieSom = energie1
        kwadratischeEnergieSom = np.square(energie1)

        for iterator in range(n-1): #We itereren over het aantal stappen, de eerste stap is hiervoor al gezet dus daarom is het n-1
            print("poging tot nieuwe configuratie")
            nieuweLijst = LijstVanAtomen(m) #een poging tot een nieuwe configuratie wordt gemaakt

            energie2 = fortran.f90.loopoverdelijst(nieuweLijst.getLijstVanAtomen(),m) #de energie van de nieuwe configuratie wordt bepaald

            energieSom += energie2
            kwadratischeEnergieSom += np.square(energie2)

            if energie1>energie2:
                optimaleconfiguratie = nieuweLijst #Als de nieuwe configuratie een lagere energie heeft, wordt dat het referentiepunt.
                print("De nieuwe energie is:")
                print(energie2)
                energie1 = energie2 #Natuurlijk moet energie1 dan aangepast worden



        stopwatch.stop()
        print("Het aanmaken van de lijsten en loopen hierover duurt zoveel seconden:")
        print(stopwatch)

        print("De som is:")
        print(energieSom)

        print("Het gemiddelde is:")
        gemiddelde = energieSom/n #n is het aantal configuraties
        print(gemiddelde)

        print("De standaardafwijking is:")
        standaardafwijking = np.sqrt(kwadratischeEnergieSom/n-np.square(energieSom/n))
        print(standaardafwijking)

        return optimaleconfiguratie.getLijstVanAtomen()

    def tijdtestenRNG (self, aantalConfiguraties=100, aantalAtomen=100):
        stopwatchNumpy = Stopwatch()
        stopwatchNumpy.start()
        for iterator in range(aantalConfiguraties):
            numpyConfiguratie = LijstVanAtomen(aantalAtomen)
        numpyTijd = stopwatchNumpy.stop()

        print("De tijd die numpy nodig heeft is (in seconden):")
        print(numpyTijd)

        stopwatchRNG = Stopwatch()
        stopwatchRNG.start()
        x = abs(rng.rngmodule.rng(12345678))
        y = abs(rng.rngmodule.rng(x))
        z = abs(rng.rngmodule.rng(y))

        xlijst = np.array(x)
        ylijst = np.array(y)
        zlijst = np.array(z)
        for iterator in range(aantalConfiguraties -1): #De loop stopt bij aantal-1 want de eerste configuratie is hierboven gemaakt.
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

        self.checkIfDuplicates_1(xlijst)
        self.checkIfDuplicates_1(ylijst)
        self.checkIfDuplicates_1(zlijst)




    def getLijstVanAtomen(self): #Deze functie geeft de lijst van atomen terug.
        return self.lijstVanAtomen #Dit geeft dus een lijst terug van 3 deellijsten, elk het aantal atomen groot.

    def checkIfDuplicates_1(self,listOfElems): #functie gepikt van internet, deze checkt of een lijst alleen unieke elementen heeft
        ''' Check if given list contains any duplicates '''
        if len(listOfElems) == len(set(listOfElems)):
            print("tis in orde")
        else:
            return print("niet in orde")


zzz = LijstVanAtomen(5)

print("test van de loop")
zzz.loopOverLijst(10,1000)
print("einde loop test")
#print("tijd testen")
#zzz.tijdtestenRNG()

