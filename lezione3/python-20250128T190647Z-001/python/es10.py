eta = int(input("Inserisci la tua età: "))
if eta < 0:
    print("Inserisci la tua vera età")
elif eta > 18 and eta < 66:
    print("Puoi partecipare all'attività")
elif eta < 18:
    print("Mi dispiace ma non hai l'età adatta per partecipare all'attività, aspetta qualche anno")
else:
    print("Mi dispiace ma non hai l'età adatta per partecipare all'attività")