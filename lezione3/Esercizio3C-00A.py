x = int(input("Inserisci quanti bambini sono nati: "))
if x < 1:
    print("Inserisci un numero valido")
else:
    match x:
        case 1:
            print("Congratulazioni!")
        case 2:
            print("Wow! Gemelli!")
        case 3:
            print("Wow! Tre!")
        case 4:
            print("Mamma mia Quattro! Wow!")
        case 5:
            print("Incredibile! Cinque!")
        case _:
            print(f"Non ci credo! {x} bambini!")