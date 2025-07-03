def main():

    lista_nomi = []

    while True:
        x = input("Inserisci il nome: ")
        if x in lista_nomi or len(lista_nomi) >= 30:
            break
        
        if x == "" or len(x) > 20:
            continue
        else:
            lista_nomi.append(x)

    print(f"Hai inserito {len(lista_nomi)} nomi distinti")
    '''
    max = lista_nomi[0]
    for i in lista_nomi:
        if len(i) > len(max):
            max = i
    print(f"Il più lungo è {max} con {len(max)} caratteri")
    '''
    s_max = max(lista_nomi, key = max)
    print(f"Il più lungo è {s_max} con {len(s_max)} caratteri")

    

if __name__ == '__main__':
    main()