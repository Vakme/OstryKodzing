#!/usr/bin/env python

# importy zewnetrzne


# nasze importy
from Menu import *
from Widok import *
from Kontroler import *
from Model import *

#===== Inicjalizacja
widok = Widok()
model = Model()
kontroler = Kontroler(widok, model)
widok.dodajKontroler(kontroler)
widok.dodajModel(model)
model.dodajKontroler(kontroler)
model.dodajWidok(widok)


#===== Start gry
widok.czyscEkran()
while not model.gracz :
    kontroler.aktualizacja(Zadania["Menu"])
widok.czyscEkran()
kontroler.glownaPetla()

