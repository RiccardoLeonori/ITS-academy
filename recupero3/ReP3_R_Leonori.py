import random

class Creatura:
    def __init__(self, nome):
        self.__nome = ""
        self.setNome(nome)

    def setNome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def getNome(self):
        return self.__nome

    def __str__(self):
        return "Creatura: " + self.__nome

class Alieno(Creatura):
    def __init__(self):
        self.__matricola = 0
        self.__munizioni = []
        self.__setMatricola()
        self.__setMunizioni()
        self._Creatura__nome = "Robot-" + str(self.__matricola)

        nome = self._Creatura__nome
        valido = True

        if len(nome) < 7:
            valido = False
        else:
            if not (nome[0] == "R" and nome[1] == "o" and nome[2] == "b" and nome[3] == "o" and nome[4] == "t" and nome[5] == "-"):
                valido = False
            else:
                parte_numerica = nome[6:]
                i = 0
                while i < len(parte_numerica):
                    if not parte_numerica[i].isdigit():
                        valido = False
                        break
                    i += 1

        if not valido:
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self._Creatura__nome = "Robot-" + str(self.__matricola)

    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self):
        self.__munizioni = []
        i = 0
        while len(self.__munizioni) < 15:
            self.__munizioni.append(i * i)
            i += 1

    def getMatricola(self):
        return self.__matricola

    def getMunizioni(self):
        return self.__munizioni

    def __str__(self):
        return "Alieno: " + self.getNome()

class Mostro(Creatura):
    def __init__(self, nome, urlo_vittoria, gemito_sconfitta):
        self.__urlo_vittoria = ""
        self.__gemito_sconfitta = ""
        self.__assalto = []
        self.__setAssalto()
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self._Creatura__nome = nome

    def __setAssalto(self):
        self.__assalto = []
        disponibili = list(range(1, 101))
        while len(self.__assalto) < 15:
            numero = random.choice(disponibili)
            if numero not in self.__assalto:
                self.__assalto.append(numero)

    def __setVittoria(self, vittoria):
        if isinstance(vittoria, str):
            self.__urlo_vittoria = vittoria
        else:
            self.__urlo_vittoria = "GRAAAHHH"

    def __setSconfitta(self, sconfitta):
        if isinstance(sconfitta, str):
            self.__gemito_sconfitta = sconfitta
        else:
            self.__gemito_sconfitta = "Uuurghhh"

    def getUrloVittoria(self):
        return self.__urlo_vittoria

    def getGemitoSconfitta(self):
        return self.__gemito_sconfitta

    def getAssalto(self):
        return self.__assalto

    def __str__(self):
        nome = self.getNome()
        alternato = ""
        i = 0
        while i < len(nome):
            c = nome[i]
            if i % 2 == 0:
                alternato += c.lower()
            else:
                alternato += c.upper()
            i += 1
        return "Mostro: " + alternato

def pariUguali(a, b):
    c = []
    i = 0
    while i < len(a) and i < len(b):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
        i += 1
    return c

def combattimento(a, m):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Errore: oggetti non validi per il combattimento.")
        return None

    confronto = pariUguali(a.getMunizioni(), m.getAssalto())
    conta = 0
    i = 0
    while i < len(confronto):
        if confronto[i] == 1:
            conta += 1
        i += 1

    if conta > 4:
        i = 0
        while i < 3:
            print(m.getUrloVittoria())
            i += 1
        return m
    else:
        print(m.getGemitoSconfitta())
        return a

def proclamaVincitore(c):
    testo = str(c)
    print("*****************************")
    print("*                           *")
    print("*     " + testo + "       *")
    print("*                           *")
    print("*****************************")

    if isinstance(c, Mostro):
        print("I Mostri hanno vinto!")
    else:
        print("Gli Alieni hanno vinto!")

def main():
    alieno = Alieno()
    print(alieno)
    print("Munizioni:", alieno.getMunizioni())

    mostro = Mostro("Gorthor", "GRAAAHHH", "Uuurghhh")
    print(mostro)
    print("Assalto:", mostro.getAssalto())

    print("\nCombattimento\n")
    vincitore = combattimento(alieno, mostro)
    if vincitore is not None:
        proclamaVincitore(vincitore)

if __name__ == "__main__":
    main()