from persona import Persona
from studente import Studente

#creo un oggetto p della classe persona

p:Persona  = Persona('Riccardo', 'Leonori', 19)

print(p)


#creo un oggetto studente1 della classe Studente
studente1: Studente = Studente("Mario", "Rossi", 20 , "0123456")

print(studente1)


#controllare se studente1 è istanza della classe Studente
#isinstance(obj, Class) -> controlla se l'oggetto obj sia instanza della classe Class    ritorna: vero/falso

if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")
else:
    print("\nstudente1 non è istanza della classe Studente")

print(isinstance(studente1, Studente))                                                  #ritorna vero


if isinstance(studente1, Persona):
    print("\nstudente1 è istanza della classe Persona")
else:
    print("\nstudente1 non è istanza della classe Persona")


if isinstance(p, Persona):
    print("\np è istanza della classe Persona")
else:
        print("\np non è istanza della classe Persona")


if isinstance(p, Studente):
    print("\np è istanza della classe Studente")
else:
    print("\np non è istanza della classe Studente")


#controllare se una classe è una sottoclasse di un altra
#issubclass(Class1, Class2) controlla se la Classe1 è sottoclasse della 2


if issubclass(Studente, Persona):
    print("\nla classe Studente è sottoclasse di Persona")
else:
    print("\nla classe Studente non è sottoclasse di Persona")