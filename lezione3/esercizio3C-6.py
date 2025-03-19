'''Esercizio 3C-6. 
Modificare il codice dell'esercizio 3C-4, affinchè si possa scrivere un codice python che consenta 
all'utente di inserire il nome di un animale ed un habitat. 
Quando il codice dell'esercizo 3C-4 classifica l'animale inserito in una delle categorie 
tra mammiferi, rettili, uccelli o pesci, oltre a mostrare un messaggio a schermo, 
deve salvare tale categoria in una variabile animal_type. 
Se l'animale inserito non è classificabile in una delle quattro categorie proposte, il valore di animal_type sarà ' "unknown".

Inserire, poi, in un dizionario il nome dell'animale, la categoria a cui esso appartiene (animal_type) e l'habitat.

Verificare con un match statement se l'animale e la categoria a cui esso appartiene possano vivere nell'habitat inserito; 
dunque, verificare:
- se l'animale può vivere nell'habitat specificato, stampare un messaggio appropriato.
- se l'habitat non è compatibile con l'habitat specificato, stampare un avviso.
- Se l'animale o l'habitat non sono riconosciuti, stampare un messaggio di errore.

Le categorie di classificazione devono essere:
- Mammiferi: cane, gatto, cavallo, elefante, leone, balena, delfino.
- Rettili: serpente, lucertola, tartaruga, coccodrillo.
- Uccelli: aquila, pappagallo, gufo, falco, cigno, anatra, gallina, tacchino.
- Pesci: squalo, trota, salmone, carpa.

Categorie di habitat:
- acqua
- aria
- terra

NOTA.
Il codice deve produrre un risultato sensato, ovvero che l'animale inserito possa effettivamente vivere nell'habitat specificato.
Tenere in considerazione il fatto che alcuni animali tra quelli specificati possono vivere in più di un habitat, 
mentre altri solo in uno.

Suggeirmento: può essere utile per coprire tutti i possibili casi implementare istruzioni match annidate.
'''


mammiferi = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci = ["squalo", "trota", "salmone", "carpa"]
habitat = ["acqua", "aria", "terra"]
animali:dict = {
    "terra": ["cane", "gatto","cavallo","elefante","leone","serpente", "lucertola", "tartaruga", "coccodrillo", "gallina", "tacchino"],
    "acqua" : ["balena", "delfino", "cigno", "anatra", "squalo", "trota", "salmone", "carpa"],
    "aria" : ["aquila", "pappagallo", "gufo", "falco"]
}

nome_animale = str(input("Digita il nome di un animale: "))
habitat_input = str(input("Digita l'habitat in cui vive l'animale: "))

match nome_animale:
    case nome_animale if nome_animale in mammiferi:
        print(f"{nome_animale} appartiene alla categoria dei Mammiferi!")
        match habitat_input:
            case habitat_input if habitat_input in animali and nome_animale in animali[habitat_input]:
                print(f"L'animale {nome_animale} può vivere nell'habitat {habitat_input}.")
            case _:
                print(f"Non ho mai visto l'animale {nome_animale} vivere nell'habitat {habitat_input}.")
    case nome_animale if nome_animale in rettili:
        print(f"{nome_animale} appartiene alla categoria dei Rettili!")
        match habitat_input:
            case habitat_input if habitat_input in animali and nome_animale in animali[habitat_input]:
                print(f"L'animale {nome_animale} può vivere nell'habitat {habitat_input}.")
            case _:
                print(f"Non ho mai visto l'animale {nome_animale} vivere nell'habitat {habitat_input}.")
    case nome_animale if nome_animale in uccelli:
        print(f"{nome_animale} appartiene alla categoria degli Uccelli!")
        match habitat_input:
            case habitat_input if habitat_input in animali and nome_animale in animali[habitat_input]:
                print(f"L'animale {nome_animale} può vivere nell'habitat {habitat_input}.")
            case _:
                print(f"Non ho mai visto l'animale {nome_animale} vivere nell'habitat {habitat_input}.")
    case nome_animale if nome_animale in pesci:
        print(f"{nome_animale} appartiene alla categoria dei Pesci!")
        match habitat_input:
            case habitat_input if habitat_input in animali and nome_animale in animali[habitat_input]:
                print(f"L'animale {nome_animale} può vivere nell'habitat {habitat_input}.")
            case _:
                print(f"Non ho mai visto l'animale {nome_animale} vivere nell'habitat {habitat_input}.")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {nome_animale}!")