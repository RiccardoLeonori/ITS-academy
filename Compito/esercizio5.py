'''Esercizio 5
Si supponga di poter acquistare barrette di cioccolato da un distributore automatico al costo di 1 euro ciascuna. 
Ogni barretta acquistata contiene un buono sconto, e con 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

Acquisisca in input un valore N (numero di euro disponibili).
Calcoli e mostri in output il numero totale di barrette che si possono ottenere, considerando anche quelle ottenute con i buoni sconto.
Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''

# calcolo quanti sono gli euro disponibili
euro = int(input("Inserisci il numero di euro disponibili: "))

barrette_acquistate = euro
# ogni barretta acquistata fornisce un buono sconto
buoni_sconto = barrette_acquistate

# calcolo delle barrette gratuite ottenute tramite buoni sconto
while buoni_sconto >= 6:
    # ogni 6 buoni sconto danno una barretta gratuita
    barrette_gratis = buoni_sconto // 6
    barrette_acquistate += barrette_gratis
    # calcolo i nuovi buoni sconto: quelli avanzati + quelli ottenuti dalle barrette gratuite
    buoni_sconto = buoni_sconto % 6 + barrette_gratis

# eseguo il print dell'output
print(f"Il numero totale di barrette acquistabili è: {barrette_acquistate}")
print(f"Il numero di buoni sconto avanzati è: {buoni_sconto}")
