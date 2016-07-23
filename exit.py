#!/usr/bin/env python

# importy zewnetrzne


# nasze importy
from Strategia import *


class exit(Strategia) :
   def pobierzDane(self, idZadania) :
      pass


   def wyslijDane(self, idZadania) :
      pass


   def main(self, czyscEkran=None) : # Argumentem jest funkcja sprzatajaca po programie
      czyscEkran()
      from sys import exit
      exit()
