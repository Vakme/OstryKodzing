#!/usr/bin/env python

# importy zewnetrzne


# nasze importy
from Stale import *


#===================================== Na czas testow
Gracz = {"nick"          :"user", 
         "haslo"         :"123", 
         "ip"            :"212.191.227.106", 
         "nazwaSerwera"  :"LocalHome"}
#===================================================#


class Model:
    def __init__(self, nowyKontroler = 0, nowyWidok = 0) :
        self.kontroler = nowyKontroler
        self.widok = nowyWidok
        self.error = 0
        self.gracz = None


    def dodajKontroler(self, nowyKontroler) :
        if self.kontroler == 0 :
            self.kontroler = nowyKontroler


    def dodajWidok(self, nowyWidok) :
        if self.widok == 0 :
            self.widok = nowyWidok


    def pobierzDane(self, idZadania, args=None) :
        if idZadania == Zadania["Login"] :
            self.zaloguj(args)


    def zaloguj(self, args) : # potrzebuje w args: [nick, haslo]
#=================================== Na czas testow
        if args[0] != Gracz["nick"] :
            self.error = Error["zlyNick"]
            return
        if args[1] != Gracz["haslo"] :
            self.error = Error["zleHaslo"]
            return
        self.gracz = Gracz
#=================================================#
        self.error = Error["brakBledow"]
