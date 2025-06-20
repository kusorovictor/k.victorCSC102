import book as bk 
import pandas as pd
import utils as ut

class Library: 
      def __init__(self):
        self.__books = []
        self.__members = []
        self.__admins = []
        
      """Adds a book to the library's collection."""   
      def add_book(self, book: bk.Book) -> bool:
        if book.isbn in [b.isbn for b in self.__books]:
          return False
        else:  
          self.__books.append(book)
          return True
        
        
          
      def remove_book(self, isbn) -> bool:
        if not ut.is_isbn(isbn):  
          raise Exception("Invalid ISBN format: ", isbn, "Please provide a valid ISBN-13.")  
        
        for book in self.__books:
          if book.isbn == isbn:
            self.__books.remove(book)
            return True
          else:
            raise Exception("Book with ISBN: ", isbn,  " not found.")
          
      def get_all_books(self):
        books_data = [{
            "Title": book.title,
            "Author": book.author,
            "ISBN": book.isbn
        } for book in self.__books]
        
        df = pd.DataFrame(books_data)
        return df
      
      def get_available_books(self):
          books_data = [{
              "Title": book.title,
              "Author": book.author,
              "ISBN": book.isbn
          } for book in self.__books if book.is_available]
                  
          df = pd.DataFrame(books_data)
          return df
        
    
      def get_book_by_isbn(self, isbn):
        if not (ut.is_isbn(isbn)):
          raise Exception("Invalid ISBN format: ", isbn, ". Please provide a valid ISBN-13.")  
        
        for book in self.__books:
          if book.isbn == isbn:
            return book
          else:
            raise Exception("Book with ISBN: ", isbn, " not found.")  


      
      def get_books_by_author(self, author):
        book_data = [{
            "Title" : book.title,
            "ISBN" : book.isbn
        } for book in self.__books if book.author == author]
        
        df = pd.DataFrame(book_data)
        return df      
      
      
      def get_books_by_title(self, title):
        book_data = [{
            "Author" : book.author,
            "ISBN" : book.isbn
        } for book in self.__books if book.title == title]
        
        df = pd.DataFrame(book_data)
        return df
      
      
      
              