# -*- coding: utf-8 -*-

"""
Module parallel_programmeren_project_olivier.parallelv1
=================================================================

Dit is de geparalleliseerde versie van lijst van atomen

"""

import numpy as np
#import scipy.constants as sc
import f2py_lijstvanatomen.lijstvanatomen as fortran
import f2py_rngfortran.rngfortran as rng
from et_stopwatch import Stopwatch
from mpi4py import MPI

class LijstVanAtomen:
    """Dit is de klasse LijstVanAtomen, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben."""


    def __init__(self, aantal): #aantal is het aantal atomen.

        lijstVanAtomen = np.random.rand(3,aantal) #Deze maakt 3 lijsten: de x-co, de y-co en de z-co

        self.lijstVanAtomen = lijstVanAtomen.reshape(3,aantal)

    def loopOverLijst(self,aantalStappen=1000,aantalAtomen=10):
        """Deze functie roept de fortranfunctie op en loopt daarover"""

        comm = MPI.COMM_WORLD
        rank = comm.Get_rank()  #huidige core
        size = comm.Get_size() #aantal cores

        n=aantalStappen     #Het aantal stappen die de simulatie neemt, er wordt 1 stap minder gedaan omdat deze al gebeurt voor de lijst te initiëren.
        m=aantalAtomen     #Het aantal atomen per lijst.

        perrank = n//size #hoeveel stappen per core, maar moet een geheel getal zijn dus //

        stopwatch = Stopwatch()
        stopwatch.start()

        energie2 = float("inf")#maximum waarde, omdat later energie1 de eerste keer kleiner moet zijn.
        energieSom = 0
        kwadratischeEnergieSom = 0

        for iterator in range(1 + rank * perrank, 1 + (rank + 1) * perrank): #We itereren over het aantal stappen
            #print("poging tot nieuwe configuratie")
            nieuweLijst = LijstVanAtomen(m) #een nieuwe configuratie wordt gemaakt

            energie1 = fortran.f90.loopoverdelijst(nieuweLijst.lijstVanAtomen,m) #de energie van de nieuwe configuratie wordt bepaald

            energieSom += energie1
            kwadratischeEnergieSom += np.square(energie1)

            if energie1<energie2: #de eerste keer wordt deze if sowieso aanvaard omdat energie2 max is, dus optimale configuratie wordt aangemaakt.

                #print("De nieuwe energie is:")
                #print(energie1)
                energie2 = energie1 #Natuurlijk moet energie2 (=laagste energie) dan aangepast worden
                optimaleconfiguratie = nieuweLijst.lijstVanAtomen #Als de nieuwe configuratie een lagere energie heeft, wordt dat het referentiepunt.

        comm.send(optimaleconfiguratie, dest=0, tag=1)
        comm.send(energie2, dest=0, tag=2)

        comm.Barrier()  # deze statement zorgt ervoor dat de core's hier zeker samen stoppen.

        stopwatch.stop()

        if rank == 0:
            optimaleconfiguratie = [optimaleconfiguratie]
            energie2 = [str(energie2)]

            for iterator in range(size-1):
                optimaleconfiguratie.append(comm.recv(source=iterator+1, tag=1))
                energie2.append(str(comm.recv(source=iterator+1, tag=2)))

            dictionary = {energie2[i]: optimaleconfiguratie[i] for i in range(len(energie2))}

            minimum = str(min(dictionary))
            optimaleconfiguratie = dictionary[minimum]


        energieSom = comm.gather(energieSom, root=0)
        kwadratischeEnergieSom = comm.gather(kwadratischeEnergieSom, root=0)

        if rank ==0:
            print("Het aanmaken van de lijsten en loopen hierover duurt zoveel seconden:")
            print(stopwatch)

            print("De som is:")
            print(sum(energieSom))

            print("Het gemiddelde is:")
            gemiddelde = sum(energieSom)/n #n is het aantal configuraties
            print(gemiddelde)

            print("De standaardafwijking is:")
            standaardafwijking = np.sqrt(sum(kwadratischeEnergieSom)/n-np.square(sum(energieSom)/n))
            print(standaardafwijking)

            return optimaleconfiguratie #probleem, returnt enkel de laagste van 0, maar wat als andere lager is?

        return 0


    def tijdtestenRNG (self, aantalConfiguraties=1000, aantalAtomen=2):
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

#print("test van de loop")
zzz.loopOverLijst(10,100)
#print("einde loop test")
#print("tijd testen")
#zzz.tijdtestenRNG()
print("einde")
