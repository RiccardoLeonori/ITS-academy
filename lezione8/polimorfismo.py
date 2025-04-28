from persona import Persona
from alieno import Alieno

#creare un oggetto p della classe Persona
p: Persona = Persona("Riccardo", "Leonori", 19)

#visualizzare le informazioni dell'oggetto p
print(p)

# creare l'oggetto et della classe alieno
et: Alieno = Alieno("Andromeda")

#visualizzare le informazioni dell'oggetto et
print(et)

# fare in modo che l'oggetto p invochi il metodo speak()
p.speak()

# fare in modo che l'oggetto et invochi il metodo speak()
et.speak()