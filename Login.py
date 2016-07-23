#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *


class login(Strategia):
    def pobierzDane(self, idZadania):  # Uzywa metod Modelu do pobrania danych z bazy, pobiera dane ze zmiennych Modelu
        self.model.pobierzDane(idZadania, (self.nick, self.haslo))  
        return not self.model.error


    def wyslijDane(self,idZadania):  # Wysyla dane do zmiennych Modelu, aktualizuje baze wywolujac odpowiednia funkcje Modelu
        pass


    def main(self, args=None):  # Glowna funkcja podprogramu
        pass


    def main(self, args=None): # Argumentem jest krotka (Model, Widok)
        self.model, self.widok, self.nick, self.haslo = args
        self.widok.czyscEkran()
        if self.pobierzDane(Zadania["Login"]) :
            print "Witaj " + self.model.gracz["nick"] + "!"
        else:
            print "Zly nick i/lub haslo!" 
