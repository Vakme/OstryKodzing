#!/usr/bin/env python

# importy zewnetrzne
from BazaDanych import *

class Gracz(BazaModel) :
    id = peewee.PrimaryKeyField()
    login = peewee.CharField()
    nick = peewee.CharField() 
    haslo = peewee.CharField()
    ip = peewee.CharField()
    pwd = peewee.CharField()
