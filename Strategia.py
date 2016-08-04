#!/usr/bin/env python

# importy zewnetrzne
import abc                       # Abstract Base Class


# nasze importy


class Strategia :                # Wszystkie Zadania powinny po niej dziedziczyc, Zadania moga miec swoje, dodatkowe metody.
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def pobierzDane(self, idZadania) :  # Uzywa metod Modelu do pobrania danych z bazy, pobiera dane ze zmiennych Modelu
        pass
   

    @abc.abstractmethod
    def wyslijDane(self, idZadania) :   # Wysyla dane do zmiennych Modelu, aktualizuje baze wywolujac odpowiednia funkcje Modelu
        pass


    @abc.abstractmethod
    def main(self, args=None) :              # Glowna funkcja podprogramu
        pass
