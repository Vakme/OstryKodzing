#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *

class cd :                 
    def pobierzDane(self, idZadania) :
        pass
  

    def wyslijDane(self, idZadania) :
        pass


    def main(self, args=None) : # (model,Args) jako argument
        if args[1] == None :
            print "cd SCIEZKA"
            return
        model = args[0]
        sciezka = args[1][0]
        if model.gracz.pwd == "/" :
            pwdKatalogi = model.gracz.pwd.split("/")
        else :
            pwdKatalogi = [""]
            pwdKatalogi.extend(model.gracz.pwd.split("/"))
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
                if "/".join(i for i in pwdKatalogi)+"/"+kat in model.serwer.pliki :
                    pwdKatalogi.append(kat)
                    ileKatalogow += 1
                else :
                    print "Nie ma takiego katalogu."
                    return
        model.gracz.pwd = "/".join(i for i in pwdKatalogi)
        if model.gracz.pwd == "" :
            model.gracz.pwd = "/"
