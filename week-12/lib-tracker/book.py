class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn 
        self.__is_available = True
        
    def __init__():    
        pass
        
        
    @property
    def title(self):
      return self.__title

    @title.setter
    def title(self, title):
      self.__title = title

    @property
    def author(self):
      return self.__author

    @author.setter
    def author(self, author):
      self.__author = author

    @property
    def isbn(self):
      return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
      self.__isbn = isbn

    @property
    def is_available(self):
      return self.__is_available

    @is_available.setter
    def is_available(self, is_available):
      self.__is_available = is_available
        