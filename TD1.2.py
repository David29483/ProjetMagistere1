#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 20:38:27 2024

@author: louislenguin
"""

#TD1.2

#%%

def max_liste(tabmax) :
    

    maximum = tabmax[0]
    
    for i in range(len(tabmax)) :
        if tabmax[i] > maximum :
            maximum = tabmax[i]
            
    return(maximum)

print(max_liste([-1,-12,-1,-3,12]))


def min_liste(tab,i1,i2):
    
    minimum = tab[i1]
    
    for i in range(i1-1,i2 ) :
        if tab[i] < minimum :
            minimum = tab[i]
        
    
    return(minimum)

print(min_liste([-1,-12,-14,-3,-1,-23],1,6))



def min_liste_ind(tab,i1,i2):
    
    minimum = tab[i1]
    ind = i1
    for i in range(i1-1,i2 ) :
        if tab[i] < minimum :
            minimum = tab[i]
            ind = i+1
    
    return(ind)

print(min_liste_ind([-121,-12,-14,-3,-1,23],1,6))

def in_liste(tab,val_in) :
    
    ind_place = None
    for i in range(len(tab)) :
        if tab[i] == val_in :
            ind_place = i+1
            break
    
    return(ind_place)
            
print(in_liste([-121,-12,-14,-3,1,23],123))
    
    
    
def tri_selection(tab) :
    
    
    ind_min = 0
    
    for i in range(len(tab)-1) :
        
        for j in range(i,lent(tab)-1) :
            
            if tab[i] < tab 
        
        
    
    
