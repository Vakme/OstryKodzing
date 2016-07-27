#!/usr/bin/env python

# nasze importy
from Strategia import *
from Stale import *

class ls :                 
    def pobierzDane(self, idZadania) :
        pass
  

    def wyslijDane(self, idZadania) :
        pass


    def main(self, args=None) : # serwer jako argument
        serwer = args[0]
        for i,j in serwer.pliki[serwer.pwd].items() :
            if j == None :
                print bcolors.BOLD+i+"\t"+bcolors.ENDC,
            elif j == Type["exec"] :
                print bcolors.OKGREEN+i+"\t"+bcolors.ENDC,
            else :
                print i+"\t",
        print ""
