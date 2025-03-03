'''
Progetta un algoritmo per ottenere la misura di un cateto c in un triangolo rettangolo, 
conoscendo quelle dell'ipotenusa a e dell'altro cateto b.'''

a = int(input("Scrivi il primo numero: "))
b = int(input("Scrivi il secondo numero: "))

if a > b:
    c = (a*a - b*b)**0.5
    print(f"Il valore dell'ipotenusa è {c:.2f}")
else:
    print("Errore")