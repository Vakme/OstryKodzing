#!/usr/bin/env python

import abc                       # Abstract Base Class

class Strategia :                # Wszystkie Zadania powinny po niej dziedziczyc, Zadania moga miec swoje, dodatkowe metody.
   __metaclass__ = abc.ABCMeta
   @abc.abstractmethod
   def pobierzDane(idZadania) :  # Uzywa metod Modelu do pobrania danych z bazy, pobiera dane ze zmiennych Modelu
      pass
   

   @abc.abstractmethod
   def wyslijDane(idZadania) :   # Wysyla dane do zmiennych Modelu, aktualizuje baze wywolujac odpowiednia funkcje Modelu
      pass


   @abc.abstractmethod
   def main(args) :              # Glowna funkcja podprogramu
      pass
