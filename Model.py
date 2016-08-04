#!/usr/bin/env python

# importy zewnetrzne
import peewee

# nasze importy
from Stale import *
from BazaDanych import *
from Gracz import *

#===================================== Na czas testow
Gracz2 = {"nick"          :"user", 
         "haslo"         :"123", 
         "ip"            :"212.191.227.106",}

Pliki =         {"/"            :None}
Pliki["/"] =    {"bin"          :None,
                 "hello.txt"    :Type["txt"]}
Pliki["/bin"] =  {"exit"        :Type["exec"],
                  "Help"        :Type["exec"],
                  "ls"          :Type["exec"],
                  "cd"          :Type["exec"]}

NazwaSerwera = "HomeSerwer"
#===================================================#

class Serwer :
    def __init__(self) :
        self.pliki = None
        self.nazwaSerwera = None
        self.ip = None
        self.pwd = '/' # sciezka do katalogu, w ktorym znajduje sie gracz


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

    def zarejestruj(self, args) : # args: [nick, haslo]
        import random
        nowyGracz = None
        while nowyGracz == None :
            a = random.randrange(1,256)
            b = random.randrange(0,256)
            c = random.randrange(0,256)
            d = random.randrange(0,256)
            noweIP = str(a)+"."+str(b)+"."+str(c)+"."+str(d)
            nowyGracz = Gracz.create(nick=args[0], haslo=args[1], ip=noweIP)
        self.zaloguj([args[0], args[1]]) 
        return True


    def zaloguj(self, args) : # potrzebuje w args: [nick, haslo]
#=================================== Na czas testow
        #if args[0] != Gracz2["nick"] :
        #    self.error = Error["zlyNick"]
        #    return False
        #if args[1] != Gracz2["haslo"] :
        #    self.error = Error["zleHaslo"]
        #    return False
        #self.gracz = Gracz2
        self.serwer.pliki = Pliki
        self.serwer.nazwaSerwera = NazwaSerwera
        #self.serwer.ip = Gracz2["ip"]
#=================================================#
        try :
            self.gracz = Gracz.get(Gracz.login == args[0])
        except Gracz.DoesNotExist as wyjatek :
            self.error = Error["zlyNick"] 
            return False
        else :
        #=== testowo ===#
            self.serwer.ip = self.gracz.ip
        #===============#
            self.error = Error["brakBledow"]
            return True
