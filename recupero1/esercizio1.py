class Frazione:
    def __init__(self, numeratore=13, denominatore=5):
        self.__numeratore = 13
        self.__denominatore = 5
        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)
    
    def get_numeratore(self):
        return self.__numeratore
    
    def get_denominatore(self):
        return self.__denominatore
    
    def set_numeratore(self, numeratore):
        if isinstance(numeratore, (int, float)) and (isinstance(numeratore, int) or numeratore.is_integer()):
            self.__numeratore = int(numeratore)
        else:
            self.__numeratore = 13
    
    def set_denominatore(self, denominatore):
        if isinstance(denominatore, (int, float)) and (isinstance(denominatore, int) or denominatore.is_integer()) and denominatore != 0:
            self.__denominatore = int(denominatore)
        else:
            self.__denominatore = 5
    
    def value(self):
        return round(self.__numeratore / self.__denominatore, 3)
    
    def __str__(self):
        return f"{self.__numeratore} / {self.__denominatore}"


def mcd(x, y):
    x, y = abs(x), abs(y)
    
    if x == 0 and y == 0:
        return 1
    if x == 0:
        return y if y > 0 else 1
    if y == 0:
        return x if x > 0 else 1
    
    while y != 0:
        x, y = y, x % y
    
    return x if x > 0 else 1


def semplifica(lista_frazioni):
    lista_semplificata = []
    
    for frazione in lista_frazioni:
        divisore_comune = mcd(frazione.get_numeratore(), frazione.get_denominatore())
        
        if divisore_comune == 1:
            lista_semplificata.append(frazione)
        else:
            nuovo_numeratore = frazione.get_numeratore() // divisore_comune
            nuovo_denominatore = frazione.get_denominatore() // divisore_comune
            frazione_semplificata = Frazione(nuovo_numeratore, nuovo_denominatore)
            lista_semplificata.append(frazione_semplificata)
    
    return lista_semplificata


def fractionCompare(lista_originale, lista_semplificata):
    for i in range(len(lista_originale)):
        valore_originale = lista_originale[i].value()
        valore_semplificato = lista_semplificata[i].value()
        print(f"Valore frazione originale: {valore_originale}, Valore frazione ridotta: {valore_semplificato}")


if __name__ == "__main__":
    l = [
        Frazione(2.5, 0),
        Frazione(1, 2),
        Frazione(2, 4),
        Frazione(3, 5),
        Frazione(6, 9),
        Frazione(4, 7),
        Frazione(24, 36),
        Frazione(12, 36),
        Frazione(40, 60),
        Frazione(5, 11),
        Frazione(10, 45),
        Frazione(42, 78),
        Frazione(9, 15)
    ]
    
    for i, frazione in enumerate(l):
        print(f"{i+1}. {frazione} = {frazione.value()}")
    
    l_s = semplifica(l)
    
    for i, frazione in enumerate(l_s):
        print(f"{i+1}. {frazione} = {frazione.value()}")
    
    fractionCompare(l, l_s)