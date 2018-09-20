# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:28:10 2018

@author: Åsne Holo
"""

"""
Deklarerer tre variabler t (tid i år), p (prosentvis endring), og befg (befolkning, gammel),
og gir dem verdier som brukeren av programmet skal putte inn.
"""

t=int(input("Hvor mange år fra i dag vil du beregne befolkningen?"))
p=float(input("Hvor mange prosent vokser/synker befolkningen med hvert år? (Skriv - foran negativ utvikling)"))
befg=int(input("Hva er den nåværende befolkningen?"))

for i in range (0, t+1): #løkke fra t=0 til t=året man ønsket å regne ut befolkningen for
   befn=befg*(1+p/100)**i #regner ut befn (befolkning, ny) til de ulike t-verdiene

print("Befolkningen etter", t, "år er", round(befn)) #skriver ut en avrunding av befn for den siste t-verdien (altså året vi ønsket å vite)