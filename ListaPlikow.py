#!/usr/bin/env python

# importy zewnetrzne
from BazaDanych import *

class ListaPlikow(BazaModel) :
    idSerwera = peewee.IntegerField()
    sciezka = peewee.CharField()
    pliki = peewee.TextField()   
