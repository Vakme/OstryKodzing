#!/usr/bin/env python

# importy zewnetrzne
from BazaDanych import *

class Serwer(BazaModel) :
    ip =  peewee.CharField()
    sciezka = peewee.CharField()
    nazwa = peewee.CharField()
    tresc = peewee.TextField()

