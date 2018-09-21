# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 11:55:48 2018

@author: Åsne Holo
"""

n=float(input("Hvilket tall vil du regne faktuleten til?")) #deklarerer en variabalen n som er tallet vi vil regne fakulteten til
a=1 #deklarerer variabelen a og gir den verdien 1 enn så lenge

if n%1==0 and n>0: #sjekker om n er et heltall, altså om resten er null når den deles på 1
    for i in range (1, round(n)+1): #løkke fra i=0 til og med i=n
        a*=i #tilegner a en ny verdi a*i for hver i fra 0 til n
    print(round(n), "!=", a) #skriver ut a
else:
    print("Tallet du skrev inn er ikke et positivt heltall, prøv igjen") #feilmelding hvis n ikke er et positivt heltall