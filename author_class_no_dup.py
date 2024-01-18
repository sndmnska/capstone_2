"""

Start with the program from part 1.

In this version, an author can't publish two books with the same name.

When the publish method is called, print an error message if 
the book given has the same name as a book currently in the books list. 
Do not add the duplicate book. (In other words, make sure the Author object's book 
list doesn't already contain that name).  

In your breakout rooms: there's more than one way to solve this - can you come up with two different solutions?

"""

class Author:
    def __init__(self, name):
        # initializes the class for what is required to create the class. 
        self.name = name
        self.books = []

    def publish(self, title):
        # Create the "publish" method.  Add a title to the "books" list for this author. 
        # Check if the book was already on the list
        if title in self.books:
            print(f"The book {title} is already in this list.")
        else:
            self.books.append(title)
    
    def __str__(self):
        return f'{self.name} has published the books: {self.books}' # I'm sure there's a better way to format this.

def main():

    shakespeare = Author ('William Shakepeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Twelfth Night')
    shakespeare.publish('Hamlet')

    print(shakespeare)
main()

## PART II:
# Prevent there being two books with the same name