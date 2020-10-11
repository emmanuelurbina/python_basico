"""
Modelo Autor
"""

class Author:
    name = None
    last_name = None

    def create_author(self,name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f"{self.name} {self.last_name}"