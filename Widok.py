#!/usr/bin/env python

# importy zewnetrzne
#from __future__ import print_function


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


   def menu(self, args=None) : # Argumentem jest funkcja czyszczaca ekran
      args()
      print "dostepne komendy:"
      print "login"
      print "exit\n"
      cmd = 0
      while True :
         cmd = raw_input()
         if cmd == "login" :                    # login
            self.czyscEkran()
            print "Nick: "
            self.nick = raw_input()
            print "Haslo: "
            self.haslo = raw_input()
            break
         elif cmd == "exit" :                   # exit
            break
         else :
            self.czyscEkran()
            print "dostepne komendy:"
            print "login"
            print "exit\n"
      if cmd == "exit" :
         self.czyscEkran()
         exit()
      self.kontroler.aktualizacja(Zadania["Login"])


   def obslugaKonsoli(self) : # Glowna petla gry, gdy juz jestesmy zalogowani
      print self.model.gracz["nick"]+"@"+self.model.gracz["nazwaSerwera"]+" ~> ", 
      cmd = raw_input() # pobieranie stringu wpisanego przez gracza
      args = None
      tab = cmd.split()
      if len(tab) > 1 :
         cmd, args = (tab[0], tab[1:]) # dzieli string na komende i jej atrybuty
      if cmd in Zadania :
         self.kontroler.aktualizacja(Zadania[cmd], args)
      else :
         self.kontroler.aktualizacja(Zadania["ZlePolecenie"], cmd)
