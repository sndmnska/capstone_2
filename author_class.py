"""

Part 1: Author class

Create a new class called Author.  Create a regular class, not a dataclass.
An Author has a name, and a list of books published.
When you create a new Author, they don't have any books. So create an empty books list attribute in the __init__ method.
Your Author class should have a publish method, which takes the title of a book as an argument. Add the title of this book to this object's books list.
Add a __str__ method that returns a String with the author's name, and the names of all of their book's titles.
Write a main function to test your class, create some example authors, and publish some example books.
"""

class Author:
    def __init__(self, name):
        # initializes the class for what is required to create the class. 
        self.name = name
        self.books = []

    def publish(self, title):
        # Create the "publish" method.  Add a title to the "books" list for this author when used.
        self.books.append(title)
    
    def __str__(self):
        return f'{self.name} has published the following books: {self.books}'

def main():

    shakespeare = Author ('William Shakepeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Twelfth Night')

    print(shakespeare)
main()