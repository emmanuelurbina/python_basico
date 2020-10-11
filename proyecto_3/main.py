"""
Emmanuel Lucio Urbina
Proyecto biblioteca
"""

from models.Author import Author
from models.Book import Book


if __name__ == "__main__":
    book = Book()
    author = Author()
    author.create_author("Emmanuel", "Lucio Urbina")

    book.create_book("IT", "123123213", author)
    print(author)
    print(book)