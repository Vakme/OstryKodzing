#/usr/bin/env python

# importy zewnetrzne


# nasze importy
from Stale import *


# importy oparte o Strategie
from ZlePolecenie import *
from exit import *
from login import *
from Menu import *


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


   def aktualizacja(self, idZadania, args=None): # analizuje dzialania usera i zleca wykonanie odpowiednich dzialan
      if idZadania == Zadania["ZlePolecenie"] :
         self.strategia = ZlePolecenie()
      elif idZadania == Zadania["Login"] :
        self.strategia = login(self.widok,self.model)
      elif idZadania == Zadania["exit"] :
         args = self.widok.czyscEkran
         self.strategia = exit()
      elif idZadania == Zadania["Menu"] :
         args = self
         self.strategia = Menu()

      if self.strategia != 0 :
         self.strategia.main(args)
      self.widok.obslugaKonsoli()