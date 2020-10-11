"""
Modelo Libro
"""


class Book():
    name = None
    isbn = None
    author = ""

    def create_book(self, name, isbn, author):
        self.name = name
        self.isbn = isbn
        self.author = author

    def __str__(self):
        return f"Libro: {self.name}\nAutor: {self.author}\nISBN: {self.isbn}"
