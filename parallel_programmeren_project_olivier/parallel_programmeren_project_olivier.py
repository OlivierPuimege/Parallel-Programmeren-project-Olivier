# -*- coding: utf-8 -*-
"""
Package parallel_programmeren_project_olivier
=======================================

A 'hello world' example.
"""
__version__ = "0.1.4"

from Atoom import Atoom
from VolledigeRuimte import VolledigeRuimte
import math
import numpy as np

def hello(who='world'):  # Laten staan voor debug
    """'Hello world' method.

    :param str who: whom to say hello to
    :returns: a string
    """
    result = "Hello " + who
    return result

testvariabele = Atoom(100,100,100)
testvariabele.testfunctie()
Atoom2 = Atoom(0,0,0)
testje = VolledigeRuimte([],[])
testje.toevoegenAtoom(testvariabele)
testje.toevoegenAtoom(Atoom2)
print("Hier zou ik alle x-coördinaten moeten uitprinten")
testje.printDeXCoordinaten()
testje.energieUpdaten()
print("Klaar")


# eof
