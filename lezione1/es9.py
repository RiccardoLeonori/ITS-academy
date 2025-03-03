'''
Progetta un algoritmo che forniti dall'utente 20 totali di vendita e i nomi dei venditori, 
trova i due nomi dei venditori con il totale più alto e il totale più basso delle vendite.'''

nome = str(input("Scrivi il nome: "))
vendite = int(input("Scrivi la vendita: "))
max_nome = nome
max = vendite
min_nome = nome
min = vendite
cont = 0
while cont < 20:
    new_nome = str(input("Scrivi il nuovo nome: "))
    new_vendite = int(input("Scrivi la vendita: "))
    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite
    else:
        if new_vendite < min:
            min_nome = new_nome
            min = new_vendite
    cont += 1
print(f"Il totale più alto è di {max_nome}, con vendite pari a {max}")
print(f"Il totale più basso è di {min_nome}, con vendite pari a {min}")