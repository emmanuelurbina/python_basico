"""
Emmanuel Lucio Urbina
Proyecto biblioteca
"""

from models.Author import Author

if __name__ == "__main__":
    author = Author()
    author.create_author("Emmanuel", "Lucio Urbina")

    print(author)