#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:38:27 2024

@author: louislenguin
"""

# Calculatrice


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
        self.fleche = self.g.afficherTexte("⬅︎", 320, 320, "white")

        self.bouton_egal = self.g.dessinerRectangle(300, 400, 50, 50, "green")
        self.egal = self.g.afficherTexte("=", 325, 425, "white")

        self.titre = self.g.afficherTexte("CALCULATRICE", 200,50,"white",26)
        self.g.actualiser()

    def Chiffre(self):
        ok = False
        valeur = input("Veuillez entrer un nombre entier : ")

        while ok != True:
            try:
                valeur = int(valeur)
                ok = True
            except ValueError:
                valeur = input("Veuillez entrer un nombre entier : ")

        return valeur


calculatrice = Calculatrice()
calculatrice.initGraph()
Fin = False
while Fin == False:

    valeur1 = calculatrice.Chiffre()
    valeur1_texte = calculatrice.g.afficherTexte(valeur1, 75, 350, "white")
    calculatrice.g.actualiser()

    calcul = None
    clic = None
    valeur2 = None

    while valeur1 == None or valeur2 == None or (calcul != calculatrice.bouton_egal and calcul != calculatrice.egal):
        clic = calculatrice.g.attendreClic()
        calcul = calculatrice.g.recupererObjet(clic.x, clic.y)

        if calcul == calculatrice.multiplication or calcul == calculatrice.division or calcul == calculatrice.addition or calcul == calculatrice.soustraction:
            valeur2 = calculatrice.Chiffre()
            calcul_final = calcul
            valeur2_texte = calculatrice.g.afficherTexte(valeur2, 200, 350, "white")

        if calcul == calculatrice.bouton_retour or calcul == calculatrice.fleche:
            if valeur2 == None:
                calculatrice.g.supprimer(valeur1_texte)
                calculatrice.g.actualiser()
                valeur1 = calculatrice.Chiffre()
                valeur1_texte = calculatrice.g.afficherTexte(valeur1, 75, 350, "white")
                calculatrice.g.actualiser()
            else:
                calculatrice.g.supprimer(valeur2_texte)
                calculatrice.g.actualiser()
                valeur2 = calculatrice.Chiffre()
                valeur2_texte = calculatrice.g.afficherTexte(valeur2, 200, 350, "white")
                calculatrice.g.actualiser()

    if calcul_final == calculatrice.multiplication or calcul_final == calculatrice.multiplication_texte:
        resultat = valeur1 * valeur2
        resultat_arrondi = round(resultat,2)
        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} x {valeur2} = {resultat_arrondi}", 175, 150, "red")
        print(resultat_arrondi)

    if calcul_final == calculatrice.addition or calcul_final == calculatrice.addition_texte:
        resultat = valeur1 + valeur2
        resultat_arrondi = round(resultat, 2)
        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} + {valeur2} = {resultat_arrondi}", 175, 150, "red")

        print(resultat_arrondi)
    if calcul_final == calculatrice.division or calcul_final == calculatrice.division_texte:
        resultat = valeur1 / valeur2
        resultat_arrondi = round(resultat, 2)
        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} / {valeur2} = {resultat_arrondi}", 175, 150, "red")

        print(resultat_arrondi)

    if calcul_final == calculatrice.soustraction or calcul_final == calculatrice.soustraction_texte:
        resultat = valeur1 - valeur2
        resultat_arrondi = round(resultat, 2)
        resultat_texte = calculatrice.g.afficherTexte(f"{valeur1} - {valeur2} = {resultat_arrondi}", 175, 150, "red")
        print(resultat_arrondi)

    annonce = calculatrice.g.afficherTexte("Cliquez n'importe où pour réaliser un autre calcul", 200, 190, "red", 8)
    calculatrice.g.actualiser()

    clic = calculatrice.g.attendreClic()
    calculatrice.g.supprimer(resultat_texte)
    calculatrice.g.supprimer(valeur1_texte)
    calculatrice.g.supprimer(valeur2_texte)
    calculatrice.g.supprimer(annonce)
    calculatrice.g.actualiser()


#dzdlkahzfpkreulh