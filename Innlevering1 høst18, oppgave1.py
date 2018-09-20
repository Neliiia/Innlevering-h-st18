# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:18:57 2018

@author: Åsne Holo
"""

from math import * #importerer biblioteket math så jeg kan bruke funksjonen log

konsentrasjon=float(input("Hva er konsentrasjonen av H^+? Svar inn på formen aeb. ")) #tilegner konsentrasjon en verdi som skal brukes i utregningen
pH=-log10(konsentrasjon) #regner ut konsentrasjonen,gir pH verdien til svaret

if 0<=pH<7:
    print("Løsningen er sur, med pH=", pH) #hvis pH er mindre enn 7: skriver ut at den er sur og svaret
elif pH==7:
    print("Løsningen er nøytral, med pH=", pH) #hvis pH er lik 7: skriver ut at den er nøytral og svaret
elif 7<pH<=14:
    print("Løsningen er basisk, med pH=", pH) #hvis pH er større enn 7: skriver ut at den er nøytral og svaret
else:
    print("Her må det være noen gale verdier, for du får et ugyldig svar...") #hvis pH har en ugyldig verdi: skriver ut at det er noe feil