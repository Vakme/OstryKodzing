#!/usr/bin/env python

# importy zewnetrzne
import peewee

# nasze importy
from Stale import *
from BazaDanych import *
from Gracz import *
from Serwer import *
from ListaPlikow import *


#===================================== Na czas testow
Gracz2 = {"nick"          :"user", 
         "haslo"         :"123", 
         "ip"            :"212.191.227.106",}

Pliki2 =         {"/"            :Type["dir"]}
Pliki2["/"] =    {"bin"          :Type["dir"],
                 "hello.txt"    :Type["txt"]}
Pliki2["/bin"] =  {"exit"        :Type["exec"],
                  "Help"        :Type["exec"],
                  "ls"          :Type["exec"],
                  "cd"          :Type["exec"]}

NazwaSerwera = "HomeServer"
#===================================================#

#class Serwer :
#    def __init__(self) :
#        self.pliki = None
#        self.nazwaSerwera = None
#        self.ip = None
#        self.pwd = '/' # sciezka do katalogu, w ktorym znajduje sie gracz


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
            self.serwer.pliki = Pliki2 # TESTOWO
            self.error = Error["brakBledow"]
            return True
