#!/usr/bin/env python

from Stale import *

class Model:
   def __init__(self, nowyKontroler = 0, nowyWidok = 0) :
      self.kontroler = nowyKontroler
      self.widok = nowyWidok
      self.error = 0
#===================================== Na czas testow
      self.gracz = {"nick":"user", "haslo":"pass123"}
#===================================================#


   def dodajKontroler(self, nowyKontroler) :
      if self.kontroler == 0 :
         self.kontroler = nowyKontroler


   def dodajWidok(self, nowyWidok) :
      if self.widok == 0 :
         self.widok = nowyWidok


   def pobierzDane(nick, haslo) :
#=================================== Na czas testow
      if nick != self.gracz["nick"] :
         self.error = Error["zlyNick"]
      if haslo != self.gracz["haslo"] :
         self.error = Error["zleHaslo"]
#=================================================#
