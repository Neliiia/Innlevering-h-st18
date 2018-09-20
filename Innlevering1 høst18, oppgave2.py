# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:59:36 2018

@author: Åsne Holo
"""

from math import *

def Ef(): #lager en funksjon som spør etter E
    global E #definerer E til å være en global variabel
    E=float(input("Hva er den kinetiske energien i J? ")) #tilegner E en float-verdi    
def mf(): #funksjon som spør etter m
    global m #m: en global variabel
    m=float(input("Hva er massen i kg? ")) #tilegner m en float-verdi
def vf(): #funksjon som spør etter v
    global v #v: global variabel
    v=float(input("Hva er farten i m/s? ")) #tilegner v en float-verdi

a=input("Vil du regne ut E, m eller v? ") #spør hva man vil regne ut

#avhengig av svaret på a, kjører programmet ett av tre mulige alternativer med funksjoner
if a=="E":
    mf()
    vf()
    E=m/2*v**2 #regner ut energien
    print("Energien er", E, "J") #printer energien
elif a=="m":
    Ef()
    vf()
    m=2*E/v**2 #regner ut massen
    print("Massen er", m, "kg") #printer massen
elif a=="v":
    Ef()
    mf()
    v=sqrt(2*E/m) #regner ut farten
    print("Farten er", v, "m/s") #printer farten
