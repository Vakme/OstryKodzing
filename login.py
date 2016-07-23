
from Strategia import *


class login(Strategia):
    def __init__(self,nowyWidok = 0, nowyModel = 0):
        self.widok=nowyWidok
        self.model=nowyModel

        self.model.pobierzDaneStare(self.widok.nick, self.widok.haslo)
        self.widok.czyscEkran()
        if self.model.error == 0:
            print "Witaj " + self.widok.nick + "!"
        else:
            print "Zly nick i/lub haslo!"


    def pobierzDane(self, idZadania):  # Uzywa metod Modelu do pobrania danych z bazy, pobiera dane ze zmiennych Modelu
        pass
    def wyslijDane(self,idZadania):  # Wysyla dane do zmiennych Modelu, aktualizuje baze wywolujac odpowiednia funkcje Modelu
        pass
    def main(self, args=None):  # Glowna funkcja podprogramu
        pass