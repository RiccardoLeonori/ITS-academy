'''#importo la classe Persona
from persona import Persona

rl:Persona = Persona("Riccardo", "Leonori", 19)

print(rl)
print(rl.name)
print(rl.last_name)
print(rl.age)

#sfrutta la funzione displayData nella classe Persona per visualizzare in output i dati relativi alla persona rl
rl.displayData()'''


from persona2 import Persona

rl:Persona = Persona()
rl.displayData()

#imposto il nome della persona rl
rl.setName("Riccardo")
rl.displayData()

#imposto il cognome della persona rl
rl.setLastname("Leonori")
rl.displayData()

#imposto il nome della persona rl
rl.setAge(-19)
rl.displayData()

print(rl.getName())
print(rl.getLastname())
print(rl.getAge())