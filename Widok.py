#!/usr/bin/env python

# importy zewnetrzne


# nasz importy
from Stale import *
from Kontroler import *


class Widok:
    def __init__(self) :
        self.kontroler = 0
        self.model = 0
        pass


    def dodajKontroler(self, nowyKontroler) :
        if self.kontroler == 0 :
            self.kontroler = nowyKontroler


    def dodajModel(self, nowyModel) :
        if self.model == 0 :
            self.model = nowyModel


    def czyscEkran(self) :
        print '\x1b[2J\x1b[H'


    def obslugaKonsoli(self) : # Glowna petla gry, gdy juz jestesmy zalogowani
        if self.model.gracz != None :
            print self.model.gracz.nick+"@"+self.model.serwer.nazwaSerwera+" "+self.model.gracz.pwd+"> ", 
        cmd = raw_input() # pobieranie stringu wpisanego przez gracza
        args = None
        tab = cmd.split()
        if len(tab) > 1 :
            cmd, args = (tab[0], tab[1:]) # dzieli string na komende i jej atrybuty
        if cmd in Zadania :
            self.kontroler.aktualizacja(Zadania[cmd], args)
        else :
            self.kontroler.aktualizacja(Zadania["ZlePolecenie"], cmd)
