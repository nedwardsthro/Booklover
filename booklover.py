import numpy as np
import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def add_book(self, book_name, book_rating):
        assert isinstance(book_name, str) == True, "book_name needs to be a string"
        assert isinstance(book_rating, int) == True, "book_rating must be an integer"
        
        if self.book_list.book_name.isin([book_name]).sum() > 0:
            pass
        else:
            new_book = pd.DataFrame({
                                    'book_name': [book_name], 
                                    'book_rating': [book_rating]
                                    })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        
    def has_read(self, book_name):
        if self.book_list.book_name.isin([book_name]).sum() > 0:
            return(True)
        else:
            return(False)
        
    def num_books_read(self):
        return(self.num_books)
    
    def fav_books(self):
        self.fav_books = self.book_list[self.book_list.book_rating > 3]
        return(self.fav_books)