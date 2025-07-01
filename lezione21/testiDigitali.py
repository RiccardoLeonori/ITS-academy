class Documento:

    testo: str

    def __init__(self, testo):
        self.setText(testo)
    
    def setText(self, testo):
        self.testo = testo

    def getText(self):
        return self.testo
    
    def isInText(self, word):
        return word in self.testo
    

class Email(Documento):
    
    mittente: str
    destinatario: str
    titolo_messaggio: str

    def __init__(self, testo, mittente, destinatario, titolo_messaggio):
        super().__init__(testo)
        self.mittente = mittente
        self.destinatario = destinatario
        self.titolo_messaggio = titolo_messaggio

    def getMittente(self):
        return self.mittente

    def setMittente(self, mittente):
        self.mittente = mittente

    def getDestinatario(self):
        return self.destinatario

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def getTitoloMessaggio(self):
        return self.titolo_messaggio

    def setTitoloMessaggio(self, titoloMessaggio):
        self.titolo_messaggio = titoloMessaggio

    def getText(self):
        return f"Da: {self.mittente}, A: {self.destinatario}\nTitolo: {self.titolo_messaggio}\nMessaggio: {self.testo}"
    
    def writeToFile(self, path: str):
        with open(path, 'w') as file:
            file.write(self.getText())

class File(Documento):

    nomePercorso: str

    def __init__(self, nomePercorso):
        self.setNomePercorso(nomePercorso)
        super().__init__(self.leggiTestoDaFile())

    def setNomePercorso(self, nomePercorso):
        self.nomePercorso = nomePercorso

    def leggiTestoDaFile(self):
        with open(self.nomePercorso, 'r') as file:
            return file.read()
        
    def getText(self):
        return f"Percorso: {self.nomePercorso}\nContenuto: {self.testo}"
    

if __name__ == '__main__':

    email = Email("Ciao come stai?", "Io", "Tu", "Saluti")
    email.writeToFile("/home/its/Scrivania/ITS/ITS-academy/ITS-academy/lezione21/prova/email.txt")

    file = File("/home/its/Scrivania/ITS/ITS-academy/ITS-academy/lezione21/prova/email.txt")
    print(file.getText())