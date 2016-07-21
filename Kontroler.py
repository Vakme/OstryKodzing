#/usr/bin/env python

from Stale import *

class Kontroler:
   def __init__(self, nowyWidok = 0, nowyModel = 0) :
      self.widok = nowyWidok
      self.model = nowyModel


   def dodajWidok(self, nowyWidok) :
      if self.widok == 0 :
         self.widok = nowyWidok


   def dodajModel(self, nowyModel) :
      if self.model == 0 :
         self.model = nowyModel


   def zaloguj(self) : 
         self.model.pobierzDane(self.widok.nick, self.widok.haslo)
         self.widok.czyscEkran()
         if self.model.error == 0 :
            print "Witaj "+self.widok.nick+"!"
         else :
            print "Zly nick i/lub haslo!"
            

   def aktualizacja(self): # analizuje dzialania usera i zleca wykonanie odpowiednich dzialan   
      idZadania = self.widok.idZadania
      if idZadania == Zadania["login"] :
            self.zaloguj()
