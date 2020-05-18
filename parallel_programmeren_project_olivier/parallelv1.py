# -*- coding: utf-8 -*-

"""
Module parallel_programmeren_project_olivier.parallelv1
=================================================================

Dit is de geparalleliseerde versie van lijst van atomen

"""

import numpy as np
import f2py_lijstvanatomen.lijstvanatomen as fortran
import f2py_rngfortran.rngfortran as rng
from et_stopwatch import Stopwatch
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

        algemeneStopwatch = Stopwatch()
        algemeneStopwatch.start()
        comm = MPI.COMM_WORLD #om iets minder te moeten typen in de rest van de code.
        rank = comm.Get_rank()  #huidige core
        size = comm.Get_size() #aantal cores

        n=aantalStappen     #Het aantal stappen die de simulatie neemt.
        m=aantalAtomen     #Het aantal atomen per lijst.

        perrank = n//size #hoeveel stappen per core, maar moet een geheel getal zijn dus //

        energie2 = float("inf")  # maximum waarde, omdat later energie1 de eerste keer kleiner moet zijn.
        energieSom = 0
        kwadratischeEnergieSom = 0

        stopwatch = Stopwatch() #Stopwatch aanmaken
        comm.Barrier()#hierdoor starten alle stopwatchen op hetzelfe moment.
        stopwatch.start()

        for iterator in range(1 + rank * perrank, 1 + (rank + 1) * perrank): #We itereren over het aantal stappen
            nieuweLijst = LijstVanAtomen(m) #een nieuwe configuratie wordt gemaakt

            energie1 = fortran.f90.loopoverdelijst(nieuweLijst.lijstVanAtomen,m) #de energie van de nieuwe configuratie wordt bepaald

            energieSom += energie1
            kwadratischeEnergieSom += energie1*energie1 #meest optimale manier

            if energie1<energie2: #de eerste keer wordt deze if sowieso aanvaard omdat energie2 max is, dus optimale configuratie wordt aangemaakt.

                energie2 = energie1 #Natuurlijk moet energie2 (=laagste energie) dan aangepast worden
                optimaleconfiguratie = nieuweLijst.lijstVanAtomen #Als de nieuwe configuratie een lagere energie heeft, wordt dat het referentiepunt.

        comm.Barrier()  # deze statement zorgt ervoor dat de core's hier zeker samen stoppen.
         #Door hiervoor samen te stoppen krijg ik enkel de traagste tijd, dus degene die de gebruiker effectief moet wachten

        #De volgende blokken zijn niet bepaald snel maar hoeven maar 1 keer uitgevoerd te worden, dus performantie-updates zijn hier verspilde moeite.

        #Deze blok dient om de optimale configuratie te vinden, tussen alle cores.
        optimaleconfiguratie = comm.gather(optimaleconfiguratie, root=0)
        energie2 = comm.gather(str(energie2),root =0)#opslaan als string opmdat dict niet kan zoeken op float
        stopwatch.stop()

        if rank ==0: #zoek de laagste energie, en geef de bijbehorende configuratie => daarom een dict.
            stopwatch1 = Stopwatch()
            stopwatch1.start()
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
            algemeneStopwatch.stop()
            stopwatch1.stop()
            print("de algemene stopwatch is:",algemeneStopwatch)
            print("stopwatch van processin in core 1",stopwatch1)
            return optimaleconfiguratie
        algemeneStopwatch.stop()

    def tijdtestenkwadraat(self, aantalIteraties=10000, getal=np.random.rand(1)):
        """
        Deze functie dient enkel om te testen of de np functies voor square en sqrt sneller zijn.
        :param aantalIteraties:
        :return:
        """

        StopwatchEigenMethode = Stopwatch()
        StopwatchEigenMethode.start()
        for iterator in range(aantalIteraties):
            getal*getal
        StopwatchEigenMethode.stop()

        StopwatchNumpy = Stopwatch()
        StopwatchNumpy.start()
        for iterator in range(aantalIteraties):
            np.square(getal)
        StopwatchNumpy.stop()

        StopwatchManueelKwadraat = Stopwatch()
        StopwatchManueelKwadraat.start()
        for iterator in range(aantalIteraties):
            getal**2
        StopwatchManueelKwadraat.stop()

        print("Stopwatch eigen methode:", StopwatchEigenMethode)
        print("Stopwatch Numpy:",StopwatchNumpy)
        print("Stopwatch Manueel kwadraat:", StopwatchManueelKwadraat)

    def tijdtestenRNG (self, aantalConfiguraties=10000, aantalAtomen=100):
        """
        Deze functie test het tijdsverschil tussen mijn rng en numpy rng
        :param aantalConfiguraties: hoeveel configuraties er doorlopen moeten worden
        :param aantalAtomen: het aantal atomen per configuratie
        :return: niets want de waardes worden geprint
        """
        stopwatchNumpy = Stopwatch()
        stopwatchNumpy.start()
        for iterator in range(aantalConfiguraties):
            numpyConfiguratie = LijstVanAtomen(aantalAtomen)
        numpyTijd = stopwatchNumpy.stop()

        print("De tijd die numpy nodig heeft is (in seconden):")
        print(numpyTijd)

        stopwatchRNG = Stopwatch()
        stopwatchRNG.start()

        xlijst = np.array(rng.rngmodule.rng(999,aantalAtomen,aantalConfiguraties))

        RNGtijd = stopwatchRNG.stop()

        print("De tijd die mijn RNG nodig heeft is (in seconden):")
        print(RNGtijd)
        self.checkIfDuplicates_1(xlijst)

    def checkIfDuplicates_1(self,listOfElems):
        """
        functie geleend van internet, deze checkt of een lijst alleen unieke elementen heeft => eigen RNg testen
        :param listOfElems:
        :return:
        """
        if len(listOfElems) == len(set(listOfElems)):
            print("Er zijn geen dubbele waardes")
        else:
            return print("niet in orde")


zzz = LijstVanAtomen(5)

#print("test van de loop")
#zzz.loopOverLijst(100,100)
#print("einde loop test")
#print("tijd testen")
zzz.tijdtestenRNG()
#print("einde")
