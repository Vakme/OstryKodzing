#!/usr/bin/env python

# importy zewnetrzne
from BazaDanych import *

class Serwer(BazaModel) :
    id =  peewee.PrimaryKeyField()
    idGracza = peewee.IntegerField()
    ip = peewee.CharField()
    nazwaSerwera = peewee.CharField()
    pliki = None
