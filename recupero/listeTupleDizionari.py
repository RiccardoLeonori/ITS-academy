'''
Liste, Tuple e Dizionari
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
2) Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.
'''

def convert(tuple):
    result = {}
    for key, value in tuple:
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result



def posneg(lista):
    risultato = {
        "positivi": [],
        "negativi": []
    }

    for numero in lista:
        if numero > 0:
            risultato["positivi"].append(numero)
        elif numero < 0:
            risultato["negativi"].append(numero)

    return risultato



def prezzo(prodotti):
    nuovi_prodotti = {}
    for nome, prezzo in prodotti.items():
        if prezzo < 50:
            prezzo_aggiornato = round(prezzo * 1.10, 2)
            nuovi_prodotti[nome] = prezzo_aggiornato
    return nuovi_prodotti