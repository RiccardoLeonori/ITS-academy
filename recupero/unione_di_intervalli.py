'''
Unione di Intervalli Sovrapposti
Data una lista di intervalli chiusi rappresentati come liste di due elementi [start, end],
scrivi una funzione merge_intervals(intervals) che restituisce una nuova lista di
intervalli in cui tutti quelli sovrapposti sono stati fusi. Ogni intervallo soddisfa start <=
end. La lista risultante deve essere ordinata per inizio intervallo e non devono esserci
sovrapposizioni.
Requisiti:
● Input: una lista di liste, ad esempio [[1, 4], [2, 6], [8, 10], [15, 18]].
● Se due intervalli si sovrappongono o si toccano (es. [1,4] e [4,5]), unirli in
[1,5].
● Restituisci una lista di intervalli fusi, ordinata per il valore di inizio.
● Casi limite:
○ Se l'input è vuoto, restituisci una lista vuota.
○ Se è presente un solo intervallo, restituiscilo così com'è.
Esempi:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals) # restituisce [[1, 6], [8, 10], [15,
18]]
intervals = [[1, 4], [4, 5]]
merge_intervals(intervals) # restituisce [[1, 5]]'''

def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    
    intervals.sort()
    risultato = [intervals[0]]
    
    for i in range(1, len(intervals)):
        ultimo = risultato[-1]
        corrente = intervals[i]
        
        if corrente[0] <= ultimo[1]:
            ultimo[1] = max(ultimo[1], corrente[1])
        else:
            risultato.append(corrente)
    
    return risultato


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]]
print(merge_intervals(intervals))

intervals = [[1, 4], [0, 2], [3, 5]]
print(merge_intervals(intervals))

intervals = []
print(merge_intervals(intervals))

intervals = [[5, 5]]
print(merge_intervals(intervals))