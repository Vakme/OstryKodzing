#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *


class Menu(Strategia) :
   def pobierzDane(self, idZadania) :
      pass


   def wyslijDane(self, idZadania) :
      pass


   def main(self, kontroler=None) : # Argumentem jest funkcja czyszczace ekran
      kontroler.widok.czyscEkran()
      print "dostepne komendy:"
      print "login"
      print "exit\n"
      cmd = 0
      while True :
         cmd = raw_input()
         if cmd == "login" :                    # login
            kontroler.widok.czyscEkran()
            print "Nick: "
            self.nick = raw_input()
            print "Haslo: "
            self.haslo = raw_input()
            break
         elif cmd == "exit" :                   # exit
            break
         else :
            self.kontroler.widok.czyscEkran()
            print "dostepne komendy:"
            print "login"
            print "exit\n"
      if cmd == "exit" :
         kontroler.widok.czyscEkran()
         kontroler.aktualizacja(Zadania["exit"])
      kontroler.aktualizacja(Zadania["Login"])


