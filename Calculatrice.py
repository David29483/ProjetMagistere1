#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:38:27 2024

@author: louislenguin
"""

#Calculatrice

from tkiteasy import *

g = ouvrirFenetre(400,600)
multiplication = g.dessinerRectangle(30,500,49,49,"white")
multiplication_texte = g.afficherTexte("x",54,525,"pink")

division = g.dessinerRectangle(131,500,49,49,"white")
division_texte = g.afficherTexte("/",155,525,"pink")

addition = g.dessinerRectangle(231,500,49,49,"white")
addition_texte = g.afficherTexte("+",255,525,"pink")

soustraction = g.dessinerRectangle(331,500,49,49,"white")
soustraction_texte = g.afficherTexte("-",355,525,"pink")

g.attendreClic()
g.actualiser()


