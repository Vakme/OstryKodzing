#/usr/bin/env python

# importy zewnetrzne


# nasze importy
from Stale import *


# importy oparte o Strategie
from ZlePolecenie import *
from exit import *
from Login import *
from Menu import *
from Help import *
from ls import *
from cd import *
from Register import *

class Kontroler:
    def __init__(self, nowyWidok = 0, nowyModel = 0) :
        self.widok = nowyWidok
        self.model = nowyModel
        self.strategia = 0


    def dodajWidok(self, nowyWidok) :
        if self.widok == 0 :
            self.widok = nowyWidok


    def dodajModel(self, nowyModel) :
        if self.model == 0 :
            self.model = nowyModel


    def glownaPetla(self) :
        while True :
            self.widok.obslugaKonsoli()
        

    def aktualizacja(self, idZadania, Args=None): # analizuje dzialania usera i zleca wykonanie odpowiednich dzialan
        args = []   # umieszczone tu zmienne wyladuja w argumentach metody main w zadaniu
        if idZadania == Zadania["ZlePolecenie"] :
            self.strategia = ZlePolecenie()
        elif idZadania == Zadania["Login"] :
            if self.model.gracz :
                self.strategia = ZlePolecenie()
            else :
                args.append(self.model)
                args.append(self.widok)
                if Args :
                    args.append(Args[0]) #nick
                    args.append(Args[1]) #haslo
                self.strategia = login()
        elif idZadania == Zadania["exit"] :
            args.append(self.widok.czyscEkran)
            self.strategia = exit()
        elif idZadania == Zadania["Menu"] :
            args.append(self)
            self.strategia = Menu()
        elif idZadania == Zadania["help"] :
            self.strategia = help()
        elif idZadania == Zadania["ls"] :
            args.append(self.model.serwer)
            self.strategia = ls()
        elif idZadania == Zadania["cd"] :
            args.append(self.model.serwer)
            args.append(Args)
            self.strategia = cd()
        elif idZadania == Zadania["Register"] :
            if self.model.gracz :
                self.strategia = ZlePolecenie()
            else :
                args.append(self)
                self.strategia = Register()
        if self.strategia != 0 :
            self.strategia.main(args)
