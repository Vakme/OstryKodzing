#!/usr/bin/env python

# importy zewnetrzne
import peewee

# nasze importy
from Stale import *
from BazaDanych import *
from Gracz import *
from Serwer import *
from ListaPlikow import *


class Model :
    def __init__(self, nowyKontroler = 0, nowyWidok = 0) :
        self.kontroler = nowyKontroler
        self.widok = nowyWidok
        self.error = 0
        self.gracz = None
        self.serwer = Serwer()

    def dodajKontroler(self, nowyKontroler) :
        if self.kontroler == 0 :
            self.kontroler = nowyKontroler


    def dodajWidok(self, nowyWidok) :
        if self.widok == 0 :
            self.widok = nowyWidok


    def pobierzDane(self, idZadania, args=None) :
        if idZadania == Zadania["Login"] :
            return self.zaloguj(args)
        return False


    def wyslijDane(self, idZadania, args=None) :
        if idZadania == Zadania["Register"] :
            return self.zarejestruj(args)

    def zarejestruj(self, args) : # args: [login, haslo]
        import random
        nowyGracz = None
        noweIP = None
        while nowyGracz == None :
            a = random.randrange(1,256)
            b = random.randrange(0,256)
            c = random.randrange(0,256)
            d = random.randrange(0,256)
            noweIP = str(a)+"."+str(b)+"."+str(c)+"."+str(d)
            nowyGracz = Gracz.create(login=args[0], nick=args[0], haslo=args[1], ip=noweIP, pwd="/")
        Serwer.create(id=nowyGracz.id, ip=noweIP, nazwaSerwera="HomeServer")
        ListaPlikow.create(idSerwera=nowyGracz.id, sciezka="/", pliki="bin;0|hello.txt;1")
        ListaPlikow.create(idSerwera=nowyGracz.id, sciezka="/bin", pliki="exit;2|help;2|ls;2|cd;2") 
        self.zaloguj([args[0], args[1]]) 
        return True


    def zaloguj(self, args) : # potrzebuje w args: [nick, haslo]
        try :
            self.gracz = Gracz.get(Gracz.login == args[0])
        except Gracz.DoesNotExist as wyjatek :
            self.error = Error["zlyNick"] 
            return False
        else :
            self.serwer = Serwer.get(Serwer.idGracza == self.gracz.id)
            for listaPlikow in ListaPlikow.select().where(ListaPlikow.idSerwera == self.serwer.id) :
                print listaPlikow
                self.serwer.pliki[listaPlikow.sciezka] = {}
                for plik in listaPlikow.pliki.split("|") :
                    nazwa, typ = plik.split(";")
                    self.serwer.pliki[listaPlikow.sciezka].setdefault(nazwa,typ)
            self.error = Error["brakBledow"]
            return True
