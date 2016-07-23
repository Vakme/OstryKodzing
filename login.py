

class login:
    def __init__(self,nowyWidok = 0, nowyModel = 0):
        self.widok=nowyWidok
        self.model=nowyModel

        self.model.pobierzDaneStare(self.widok.nick, self.widok.haslo)
        self.widok.czyscEkran()
        if self.model.error == 0:
            print "Witaj " + self.widok.nick + "!"
        else:
            print "Zly nick i/lub haslo!"
