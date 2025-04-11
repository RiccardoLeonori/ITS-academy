class Libro:
    def _init_(self):
        self.titolo:str = ""
        self.autore:str = ""
        self.genere:list[str] = []

    def set_titolo(self, titolo:str) -> None:
        self.titolo = titolo

    def set_autore(self, nome:str) -> None:
        self.autore = nome

    def set_genere(self, tipo_genere:list[str]) -> None:
        self.genere = tipo_genere

    def get_titolo(self) -> str:
        return self.titolo
    
    def get_autore(self) -> str:
        return self.autore
    
    def get_genere(self) ->list[str]:
        return self.genere
    
class Biblioteca:
    def _init_(self):
        self.libri:list[Libro] = []

    def set_libro(self, libro:Libro) -> None:
        self.libri.append(libro)

    def get_info(self) ->str:
        for item in self.libri:
            print(item.get_titolo(), item.get_autore(), item.get_genere())

# codice driver
collezione:Biblioteca = Biblioteca()

#libro 1
libro1:Libro = Libro()
libro1.set_titolo("Il piccolo principe")
libro1.set_autore("Sconosciuto")
libro1.set_genere(["Narrativa", "Qualcosa"])

collezione.set_libro(libro1)

#libro 2
libro2:Libro = Libro()
libro2.set_titolo("Harry potter")
libro2.set_autore("J.K. Rowling")
libro2.set_genere(["Narrativa", "Fantasy"])

collezione.set_libro(libro2)

collezione.get_info()