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

        self.bouton_retour = self.g.dessinerRectangle(300, 300, 50, 50, "red")
        self.fleche = self.g.afficherTexte("⬅︎", 320, 320, "pink")

        self.g.actualiser()

    def PremierChiffre(self):
        ok = False
        self.valeur1 = input("Veuillez entrer un nombre entier : ")

        while ok != True:
            try:
                self.valeur1 = int(self.valeur1)
                ok = True
            except ValueError:
                self.valeur1 = input("Veuillez entrer un nombre entier : ")

        self.valeur1_texte = calculatrice.g.afficherTexte(self.valeur1, 75, 350, "white")
        calculatrice.g.actualiser()


calculatrice = Calculatrice()
calculatrice.initGraph()
Fin = False
while Fin == False:

    calculatrice.PremierChiffre()
    calcul = None
    clic = None

    while calcul != calculatrice.multiplication and calcul != calculatrice.division and calcul != calculatrice.addition and calcul != calculatrice.soustraction:
        clic = calculatrice.g.attendreClic()
        calcul = calculatrice.g.recupererObjet(clic.x, clic.y)

        if calcul == calculatrice.bouton_retour or calcul == calculatrice.fleche:
            calculatrice.g.supprimer(calculatrice.valeur1_texte)
            calculatrice.g.actualiser()
            calculatrice.PremierChiffre()

    valeur2 = input("Veuillez entrer un nombre entier : ")
    ok = False
    while ok != True:
        try:
            valeur2 = int(valeur2)
            ok = True
        except ValueError:
            valeur2 = input("Veuillez entrer un deuxième nombre entier : ")

    valeur2_texte = calculatrice.g.afficherTexte(valeur2, 200, 350, "white")

    if calcul == calculatrice.multiplication or calcul == calculatrice.multiplication_texte:
        resultat = calculatrice.valeur1 * valeur2
        print(resultat)
        calculatrice.g.afficherTexte(f"{calculatrice.valeur1} x {valeur2} = {resultat}", 150, 150, "red")

    if calcul == calculatrice.addition or calcul == calculatrice.addition_texte:
        resultat = calculatrice.valeur1 + valeur2
        print(resultat)

        calculatrice.g.afficherTexte(f"{calculatrice.valeur1} + {valeur2} = {resultat}", 150, 150, "red")

    if calcul == calculatrice.division or calcul == calculatrice.division_texte:
        resultat = calculatrice.valeur1 / valeur2
        print(resultat)

        calculatrice.g.afficherTexte(f"{calculatrice.valeur1} / {valeur2} = {resultat}", 150, 150, "red")

    if calcul == calculatrice.soustraction or calcul == calculatrice.soustraction_texte:
        resultat = calculatrice.valeur1 - valeur2
        print(resultat)

        calculatrice.g.afficherTexte(f"{calculatrice.valeur1} - {valeur2} = {resultat}", 150, 150, "red")

    calculatrice.g.actualiser()
    clic = calculatrice.g.attendreClic()

