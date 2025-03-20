class Persona:
    def __init__(self):
        self.name = ""
        self.last_name = ""
        self.age = 0
    def displayData(self) -> None:
        print(f"nome: {self.name}\ncognome: {self.last_name}\netà: {self.age}")
    
    #funzione che consente di impostare il valore di self.name
    def setName(self, name:str) -> None:
        self.name = name

    def setLastname(self, last_name:str) -> None:
        self.last_name = last_name

    def setAge(self, age:int) -> None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    #funzione che mi restituisce il valore di self.name
    def getName(self) -> str:
        return self.name
    
    def getLastname(self) -> str:
        return self.last_name
    
    def getAge(self) -> int:
        return self.age