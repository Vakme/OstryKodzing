#!/usr/bin/env python

from Stale import *
from Kontroler import *

class Widok:
   def __init__(self, nowyKontroler = 0, nowyModel = 0) :
      self.kontroler = nowyKontroler
      self.model = nowyModel
      self.idZadania = 0                                 # ID danych, ktore kontroler musi pobrac


   def dodajKontroler(self, nowyKontroler) :
      if self.kontroler == 0 :
         self.kontroler = nowyKontroler


   def dodajModel(self, nowyModel) :
      if self.model == 0 :
         self.model = nowyModel


   def powiadomKontroler(self, noweIdZadania) : # Na podstawie idZadania Kontroler pobiera dane z Widoku
      if type(self.kontroler) == type(Kontroler) :
         self.idZadania = noweIdZadania
         self.kontroler.aktualizacja()


   def czyscEkran(self) :
      # print '\033[2j\033[0;0h'
      print '\x1b[2J\x1b[H'


   def menu(self) :
      self.czyscEkran()
      print "dostepne komendy:"
      print "login"
      print "exit"
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
            print "exit"
      if cmd == exit :
         self.czyscEkran()
         exit()
      self.powiadomKontroler(Zadania["login"])
