#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *

class ls :                 
    def pobierzDane(self, idZadania) :
        pass
  

    def wyslijDane(self, idZadania) :
        pass


    def main(self, args=None) : # model jako argument
        model = args[0]
        for i,j in model.serwer.pliki[model.gracz.pwd].items() :
            if j == Type["dir"] :
                print bcolors.BOLD+i+"\t"+bcolors.ENDC,
            elif j == Type["exec"] :
                print bcolors.OKGREEN+i+"\t"+bcolors.ENDC,
            else :
                print i+"\t",
        print ""
