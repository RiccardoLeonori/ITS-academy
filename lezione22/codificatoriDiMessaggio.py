from abc import ABC, abstractmethod


class CodificatoreMessaggio:

    @abstractmethod
    def codifica(testoInChiaro):
        pass


class DecodificatoreMessaggio:

    @abstractmethod
    def decodifica(testoCodificato):
        pass


class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    
    def __init__(self, chiave):
        super().__init__()
        self.chiave = chiave

    def codifica(self, testoInChiaro):
        r = []
        for c in testoInChiaro:
            if c.isalpha():
                o = ord('A') if c.isupper() else ord('a')
                r.append(chr((ord(c) - o + self.chiave) % 26 + o))       
            else:
                r.append(c)
        return ''.join(r)
    
    def decodifica(self, testoCifrato):
        r = []
        for c in testoCifrato:
            if c.isalpha():
                o = ord('A') if c.isupper() else ord('a')
                r.append(chr((ord(c) - o - self.chiave) % 26 + o))       
            else:
                r.append(c)
        return ''.join(r)
    
    
class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n):
        super().__init__()
        self.n = n

    def codifica(self, testoInChiaro):
        testo = testoInChiaro
        for j in range(self.n):
            meta = (len(testo) + 1) // 2
            prima = testo[:meta]
            seconda = testo[meta:]
            combinato = ""
            for i in range(len(prima)):
                combinato += prima[i]
                if i < len(seconda):
                    combinato += seconda[i]
            testo = combinato
        return testo
    
    def decodifica(self, testoCodificato):
        for i in range(self.n):
            testo = testoCodificato
            prima = testoCodificato[::2]
            seconda = testoCodificato[1::2]
            testo = prima + seconda
            testoCodificato = testo
        return testo

c = CifratoreACombinazione(2)
print(c.codifica("abcdefghi"))

d = CifratoreACombinazione(2)
print(d.decodifica("ahfdbigec"))