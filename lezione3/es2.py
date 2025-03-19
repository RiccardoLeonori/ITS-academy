def semaforo_intelligente(veicoli_ns, veicoli_eo, soglia=70, tempo_minimo=60):
    if veicoli_ns > soglia and veicoli_eo > soglia:
        verde_ns = 50
        verde_eo = 50
    elif veicoli_ns > soglia:
        verde_ns = tempo_minimo
        verde_eo = 100 - verde_ns
    elif veicoli_eo > soglia:
        verde_eo = tempo_minimo
        verde_ns = 100 - verde_eo
    else:
        totale_veicoli = veicoli_ns + veicoli_eo
        verde_ns = (veicoli_ns / totale_veicoli) * 100
        verde_eo = 100 - verde_ns
        if verde_eo == 100:
            verde_eo = 99
            verde_ns = 1
        else:
            verde_ns = 99
            verde_eo = 1


    print(f"Tempo verde per la direzione Nord-Sud: {verde_ns:.2f}%")
    print(f"Tempo verde per la direzione Est-Ovest: {verde_eo:.2f}%")


semaforo_intelligente(60, 0)
