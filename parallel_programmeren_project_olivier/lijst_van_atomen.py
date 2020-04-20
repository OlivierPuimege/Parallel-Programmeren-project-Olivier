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

    def loopOverLijst(self):
        """Deze functie roept de fortranfunctie op en loopt daarover"""

        fortran.f90.loopoverdelijst(self.lijstVanAtomen)



    def getLijstVanAtomen(self):
        return self.lijstVanAtomen
