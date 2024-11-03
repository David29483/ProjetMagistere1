#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:38:27 2024

@author: louislenguin
"""

#Calculatrice


from tkiteasy import *


class Calculatrice():
    def __init__(self):
        self.g = ouvrirFenetre(400, 600)
        self.g.dessinerRectangle(30, 500, 49, 49, "white")

    def initGraph(self):
        self.multiplication = self.g.dessinerRectangle(30, 500, 49, 49, "white")
        self.multiplication_texte = self.g.afficherTexte("x", 54, 525, "pink")

        self.division = self.g.dessinerRectangle(131, 500, 49, 49, "white")
        self.division_texte = self.g.afficherTexte("/", 155, 525, "pink")

        self.addition = self.g.dessinerRectangle(231, 500, 49, 49, "white")
        self.addition_texte = self.g.afficherTexte("+", 255, 525, "pink")

        self.soustraction = self.g.dessinerRectangle(331, 500, 49, 49, "white")
        self.soustraction_texte = self.g.afficherTexte("-", 355, 525, "pink")

        self.affiche_valeur1 = self.g.dessinerRectangle(30, 300, 100, 100, "blue")
        self.affiche_valeur2 = self.g.dessinerRectangle(150, 300, 100, 100, "blue")

        self.affiche_resultat = self.g.dessinerRectangle(100, 100, 200, 100, "white")
        self.g.actualiser()


calculatrice = Calculatrice()
calculatrice.initGraph()
i = 0
Fin = False
while Fin == False:
    ok = False
    valeur1 = input("Veuillez entrer un nombre entier : ")

    while ok != True:
        try:
            valeur1 = int(valeur1)
            ok = True
        except ValueError:
            valeur1 = input("Veuillez entrer un nombre entier : ")

    valeur1_texte = calculatrice.g.afficherTexte(valeur1, 75, 350, "white")
    calculatrice.g.actualiser()

    calcul = None
    clic = None

    while calcul != calculatrice.multiplication and calcul != calculatrice.division and calcul != calculatrice.addition and calcul != calculatrice.soustraction:
        clic = calculatrice.g.attendreClic()
        calcul = calculatrice.g.recupererObjet(clic.x, clic.y)


    valeur2 = input("Veuillez entrer un nombre entier : ")
    ok = False
    while ok != True:
        try:
            nombre = int(valeur2)
            ok = True
        except ValueError:
            valeur2 = input("Veuillez entrer un deuxième nombre entier : ")

    valeur2_texte = calculatrice.g.afficherTexte(valeur2, 200, 350, "white")
    resultat = 0

    if i > 0 :
      calculatrice.g.supprimer(resultat_texte)

    if calcul == calculatrice.multiplication or calcul == calculatrice.multiplication_texte:
        resultat = int(valeur1) * int(valeur2)
        print(resultat)

        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} x {valeur2} = {resultat}", 150, 150, "red")

        calculatrice.g.supprimer(valeur2_texte)
        calculatrice.g.supprimer(valeur1_texte)
        i +=1

    if calcul == calculatrice.addition or calcul == calculatrice.addition_texte:
        resultat = int(valeur1) + int(valeur2)
        print(resultat)
        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} + {valeur2} = {resultat}", 150, 150, "red")

        calculatrice.g.supprimer(valeur2_texte)
        calculatrice.g.supprimer(valeur1_texte)
        i = i+1

    if calcul == calculatrice.division or calcul == calculatrice.division_texte:
        resultat = int(valeur1) / int(valeur2)

        print(resultat)

        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} / {valeur2} = {resultat}", 150, 150, "red")
        calculatrice.g.supprimer(valeur2_texte)
        calculatrice.g.supprimer(valeur1_texte)
        i = i+1

    if calcul == calculatrice.soustraction or calcul == calculatrice.soustraction_texte:
        resultat = int(valeur1) - int(valeur2)

        print(resultat)

        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} - {valeur2} = {resultat}", 150, 150, "red")
        calculatrice.g.supprimer(valeur2_texte)
        calculatrice.g.supprimer(valeur1_texte)
        i = i+1

    calculatrice.g.actualiser()
    clic = calculatrice.g.attendreClic()

