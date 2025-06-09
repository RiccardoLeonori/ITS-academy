def cifra_cesare(testo, chiave):
    risultato = ""
    for carattere in testo:
        if carattere.isalpha():
            if carattere.isupper():
                nuovo_carattere = chr((ord(carattere) - ord('A') + chiave) % 26 + ord('A'))
            else:
                nuovo_carattere = chr((ord(carattere) - ord('a') + chiave) % 26 + ord('a'))
            risultato += nuovo_carattere
        else:
            risultato += carattere
    return risultato

def decifra_cesare(testo_cifrato, chiave):
    return cifra_cesare(testo_cifrato, -chiave)

def forza_bruta_cesare(testo_cifrato):
    risultati = {}
    for chiave in range(26):
        risultati[chiave] = decifra_cesare(testo_cifrato, chiave)
    return risultati

if __name__ == "__main__":
    testo_originale = "Ciao, mondo! Come stai?"
    chiave = 3
    
    print(f"Testo originale: {testo_originale}")
    print(f"Chiave: {chiave}")
    
    testo_cifrato = cifra_cesare(testo_originale, chiave)
    print(f"Testo cifrato: {testo_cifrato}")
    
    testo_decifrato = decifra_cesare(testo_cifrato, chiave)
    print(f"Testo decifrato: {testo_decifrato}")
    
    print("\n" + "="*50)
    print("FORZA BRUTA - Tutte le possibili decifrazioni:")
    print("="*50)
    
    testo_segreto = "Fldr, prqgr!"
    print(f"Testo da decifrare: {testo_segreto}")
    print()
    
    risultati = forza_bruta_cesare(testo_segreto)
    for k, v in risultati.items():
        print(f"Chiave {k:2d}: {v}")