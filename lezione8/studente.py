from persona import Persona

#la classe studente eredita dalla classe persona
class Studente(Persona):

    '''
    Attributi  della classe Persona in quanto eredita da Persona
    self.name: str
    self.lastname: str
    self.age: int

    Attributi dello studente
    self.matricola: str
    '''


    def __init__(self, name: str, lastname: str, age: int, matricola: str):
        # inizializzo la classe Persona richiamando il metodo __init__ della superclasse
        super().__init__(name , lastname, age)

        # istruzioni che inizializzano un oggetto della classe Studente
        self.setMatricola(matricola)


    def __str__(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}\nMatricola: {self.matricola}"
    

    def setMatricola(self, matricola: str) ->None:
        if matricola:
            self.matricola= matricola
        else:
            print("Errore!!! Il campo matricola non può essere vuoto!")

    
    def getMatricola(self) ->str:
        return self.matricola