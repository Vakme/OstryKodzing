#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *

class cd :                 
    def pobierzDane(self, idZadania) :
        pass
  

    def wyslijDane(self, idZadania) :
        pass


    def main(self, args=None) : # (serwer,Args) jako argument
        if args[1] == None :
            print "cd SCIEZKA"
            return
        serwer = args[0]
        sciezka = args[1][0]
        if serwer.pwd == "/" :
            pwdKatalogi = serwer.pwd.split("/")
        else :
            pwdKatalogi = [""]
            pwdKatalogi.extend(serwer.pwd.split("/"))
        pwdKatalogi.remove("")
        ileKatalogow = len(pwdKatalogi)
        katalogi = sciezka.split("/")
        if katalogi[0] == "" :
            katalogi.remove("")
        for kat in katalogi :
            if kat == ".." :
                if ileKatalogow == 1 :
                    continue
                else :
                    pwdKatalogi.remove(pwdKatalogi[-1])
                    ileKatalogow -= 1 
            else :
                if "/".join(i for i in pwdKatalogi)+"/"+kat in serwer.pliki :
                    pwdKatalogi.append(kat)
                    ileKatalogow += 1
                else :
                    print "Nie ma takiego katalogu."
                    return
        serwer.pwd = "/".join(i for i in pwdKatalogi)
        if serwer.pwd == "" :
            serwer.pwd = "/"
