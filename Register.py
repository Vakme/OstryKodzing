#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *

class Register : 
    def pobierzDane(self, idZadania) :
        pass


    def wyslijDane(self, idZadania) :
        #if idZadania == Zadania["register"] :
        self.kontroler.model.wyslijDane(Zadania["Register"], 
                                       [self.nick, self.haslo])


    def main(self, args=None) : # args: [kontroler]
        self.kontroler = args[0]
        self.kontroler.widok.czyscEkran()
        print "Nick: ",
        self.nick = raw_input()
        while True :
            print "Haslo: ",
            self.haslo = raw_input()
            print "Powtorz haslo: ",
            self.haslo2 = raw_input()
            if self.haslo != self.haslo2 :
                self.kontroler.widok.czyscEkran()
                print "Hasla nie pokrywaja sie!"
                continue
            break
        self.wyslijDane(Zadania["Register"])
        return
