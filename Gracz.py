#!/usr/bin/env python

# importy zewnetrzne
from BazaDanych import *

class Gracz(BazaModel) :
    id = peewee.PrimaryKeyField()
    nick = peewee.CharField() 
    haslo = peewee.CharField()
    ip = peewee.CharField()
