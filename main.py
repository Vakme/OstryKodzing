#!/usr/bin/env python

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



#===== Logowanie
widok.menu()

