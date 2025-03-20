"""
booklover.py
"""

import pandas as pd 

class BookLover(): 
    """
    This class provides attributes and methods that represent a "book lover." 
    Captured attributes include a person's name, email, favorite book genre, 
    the number of books they've read, and a list of the books they've read. 
    
    The methods provided allow a user to: 
    (1) add books to a book list, 
    (2) check whether a book has been read previously, 
    (3) return the number of books read, and
    (4) filter down the book list to favorite books (books with rating > 3) 
    """
    
    # Initializer
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        """Class constructor"""
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    # Method 1
    def add_book(self, book_name, book_rating): 
        """Add a book to the book list if it's not already in the list."""
        if self.book_list['book_name'].isin([book_name]).any():
            print("This book is already in the list and cannot be added.") 
        else: 
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books+=1
    
    # Method 2
    def has_read(self, book_name):
        """Check if the person has already read the book."""
        if self.book_list['book_name'].isin([book_name]).any():
            return True
        else: 
            return False
        
    # Method 3
    def num_books_read(self):
        """Return the number of books the person has read."""
        return self.num_books
    
    # Method 4
    def fav_books(self):
        """Return the person's favorite books (those with rating higher than 3)."""
        return self.book_list[self.book_list['book_rating'] > 3]
            
if __name__ == '__main__':
    # prototype class 

    # create object
    my_object = BookLover("Claire D", "ced123@gmail.com", "romance")
    print("Book Lover Name: ", my_object.name, ", Email: ", my_object.email, ", Favorite Genre: ", my_object.fav_genre, "\n", sep = "")
    my_object.add_book("Pride and Prejudice", 5)
    my_object.add_book("Emma", 5)
    my_object.add_book("Persuasion", 5)
    my_object.add_book("Sense and Sensibility", 4.5)
    my_object.add_book("Northanger Abbey", 4)
    my_object.add_book("Mansfield Park", 3)
    
    # get book list
    print(my_object.name, "'s books: \n", my_object.book_list, "\n")
    
    # check has_read method
    print("Read 'Persuasion'? ", my_object.has_read("Persuasion"), "\n")
    print("Read 'Lady Susan'? ", my_object.has_read("Lady Susan"), "\n")
    
    # check num_books_read method
    print("Number of books read: ", my_object.num_books_read(), "\n", sep = "")
    
    # check fav_books method 
    print(my_object.name, "'s favorite books: \n", my_object.fav_books(), sep = "")