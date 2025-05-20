from typing import Self

class Book:
    def __init__(self, title: str, autor: str, isbn: str):
        self._title = title
        self._autor = autor
        self._isbn = isbn

    def __str__(self) -> str:
        return f"Il titolo è {self._title}, l'autore è {self._autor} e l'isbn è {self._isbn}"
    

    @classmethod
    def from_string(cls, repr_str: str) -> Self:
        sub_strs = repr_str.split(',')
        return cls(sub_strs[0], sub_strs[1], sub_strs[2])