# -*- coding: utf-8 -*-

"""
Module parallel_programmeren_project_olivier.final
=================================================================
Dit is de versie zonder timing code, dus de versie die in praktijk gebruikt zou kunnen worden.
"""

import numpy as np
import f2py_lijstvanatomen.lijstvanatomen as fortran
import f2py_rngfortran.rngfortran as rng
from mpi4py import MPI

class LijstVanAtomen:
    """
    Dit is de klasse LijstVanAtomen, omdat we enkel Lennard-Jones potentialen gaan gebruiken moet deze enkel positites hebben.
    """

    def __init__(self, aantal):
        """
        Deze maakt een klasseobject aan van lijst van atomen.
        De coördinaten staan allemaal in 1 lijst. Dus de fortranfunctie moet voor y-coördinaten het aantal atoomnummer
        plus het aantal atomen moeten doen, en voor z + 2 keer het aantal atomen. De vorm van de lijst is dus
        [x1,x2,...,y1,y2,...,z1,z2,...]
        :param aantal: Hoeveel atomen er in de gewenste sample moeten zijn.
        """
        self.lijstVanAtomen = np.random.rand(3*aantal) #Deze maakt 1 lijst: eerst alle x-co, dan alle y-co,... Dat is wel puur een pragmatische keuze.

    def loopOverLijst(self,aantalStappen=100,aantalAtomen=1000):
        """
        Deze functie roept de fortranfunctie op en loopt daarover, en geeft een aantal resultaten weer, zoals hoe lang de loop duurde.
        :param aantalStappen: Hoeveel configuraties er getest worden.
        :param aantalAtomen:  Hoeveel atomen er per configuratie moeten zijn
        :return: De optimale configuratie wordt teruggegeven
        """

        comm = MPI.COMM_WORLD #om iets minder te moeten typen in de rest van de code.
        rank = comm.Get_rank()  #huidige core
        size = comm.Get_size() #aantal cores

        n=aantalStappen     #Het aantal stappen die de simulatie neemt.
        m=aantalAtomen     #Het aantal atomen per lijst.

        perrank = n//size #hoeveel stappen per core, maar moet een geheel getal zijn dus //

        energie2 = float("inf")  # maximum waarde, omdat later energie1 de eerste keer kleiner moet zijn.
        energieSom = 0
        kwadratischeEnergieSom = 0


        for iterator in range(1 + rank * perrank, 1 + (rank + 1) * perrank): #We itereren over het aantal stappen
            nieuweLijst = LijstVanAtomen(m) #een nieuwe configuratie wordt gemaakt

            energie1 = fortran.f90.loopoverdelijst(nieuweLijst.lijstVanAtomen,m) #de energie van de nieuwe configuratie wordt bepaald

            energieSom += energie1
            kwadratischeEnergieSom += energie1*energie1 #meest optimale manier

            if energie1<energie2: #de eerste keer wordt deze if sowieso aanvaard omdat energie2 max is, dus optimale configuratie wordt aangemaakt.

                energie2 = energie1 #Natuurlijk moet energie2 (=laagste energie) dan aangepast worden
                optimaleconfiguratie = nieuweLijst.lijstVanAtomen #Als de nieuwe configuratie een lagere energie heeft, wordt dat het referentiepunt.

        #De volgende blokken zijn niet bepaald snel maar hoeven maar 1 keer uitgevoerd te worden, dus performantie-updates zijn hier verspilde moeite.

        #Deze blok dient om de optimale configuratie te vinden, tussen alle cores.
        optimaleconfiguratie = comm.gather(optimaleconfiguratie, root=0)
        energie2 = comm.gather(str(energie2),root =0)#opslaan als string opmdat dict niet kan zoeken op float

        if rank ==0: #zoek de laagste energie, en geef de bijbehorende configuratie => daarom een dict.
            dictionary = {energie2[i]: optimaleconfiguratie[i] for i in range(len(energie2))}

            minimum = str(min(dictionary)) #normaal kan python dit aan, maar min geeft wel een getal terug, dus vandaar opnieuw een string.
            optimaleconfiguratie = dictionary[minimum]

        energieSom = comm.gather(energieSom, root=0)
        kwadratischeEnergieSom = comm.gather(kwadratischeEnergieSom, root=0)
        if rank == 0:

            print("Het aanmaken van de lijsten en loopen hierover duurt zoveel seconden:")
            print(stopwatch)

            print("De som is:")
            print(sum(energieSom))

            print("Het gemiddelde is:")
            gemiddelde = sum(energieSom)/n #n is het aantal configuraties
            print(gemiddelde)

            print("De standaardafwijking is:")
            standaardafwijking = np.sqrt(sum(kwadratischeEnergieSom)/n-np.square(gemiddelde))
            print(standaardafwijking)

            return optimaleconfiguratie
    

  


