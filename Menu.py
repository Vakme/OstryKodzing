#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *


class Menu(Strategia) :
    def pobierzDane(self, idZadania) :
        pass


    def wyslijDane(self, idZadania) :
        pass


    def komendy(self) : 
        self.kontroler.widok.czyscEkran()
        print "dostepne komendy:"
        print "login"
        print "register"
        print "exit\n"


    def main(self, args=None) : # Argumentem jest funkcja czyszczace ekran
        self.kontroler = args[0]
        self.komendy()
        cmd = None
        while True :
            cmd = raw_input()
            
            if cmd == "login" :                    # login
                self.kontroler.widok.czyscEkran()
                print "Nick: ",
                self.nick = raw_input()
                print "Haslo: ",
                self.haslo = raw_input()
                self.kontroler.aktualizacja(Zadania["Login"], 
                                           (self.nick, self.haslo))
                return
            elif cmd == "register" :
                self.kontroler.aktualizacja(Zadania["Register"]) 
                return
            elif cmd == "exit" :                   # exit
                self.kontroler.widok.czyscEkran()
                self.kontroler.aktualizacja(Zadania["exit"])
                return
            else :
                self.komendy()


