class Book:
    def __init__(self, title, author): 
        self.__title = title      
        self.__author = author
        self.__is_issued = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_issued(self):
        return self.__is_issued

    def issue(self): #function to issue any book to student or faculty
        if not self.__is_issued:
            self.__is_issued = True
            return True
        return False

    def return_book(self): #function to return book by students or faculty
        if self.__is_issued:
            self.__is_issued = False
            return True
        return False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book): #function to borrow book
        if book.issue():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.get_title()}'.")
        else:
            print(f"'{book.get_title()}' is already issued.")

    def return_book(self, book): #function to return book
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.get_title()}'.")
        else:
            print(f"{self.name} does not have '{book.get_title()}'.")



class StudentMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.limit = 5

    def borrow_book(self, book): #check if student can borrow the book
        if len(self.borrowed_books) < self.limit:
            super().borrow_book(book)
        else:
            print(f"{self.name} cannot borrow more than {self.limit} books.")


class FacultyMember(Member):
    def __init__(self, name):
        super().__init__(name)
        self.limit = 7

    def borrow_book(self, book): #check if faculty can borrow the book
        if len(self.borrowed_books) < self.limit:
            super().borrow_book(book)
        else:
            print(f"{self.name} cannot borrow more than {self.limit} books.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book): # adds new book to the library system
        self.books.append(book)

    def show_available_books(self): #shows the list of current books available in the library
        print("\nAvailable Books:")
        for book in self.books:
            if not book.is_issued():
                print(f"- {book.get_title()} by {book.get_author()}")
      
   
if __name__ == "__main__":
    lib = Library()
    b1 = Book("Engineering mathematics", "K.A. Stroud") #list of book and their authors
    b2 = Book("Basic Civil Engineering", "B.C. Punmia, Ashok Kumar Jain, Arun Kumar Jain")
    b3 = Book("Basic Mechanical Engineering ", "Pravin Kumar")
    b4 = Book("Clean Code","Robert C. Martin")
    b5 = Book("The Phoenix Project","Gene Kim")
    
    lib.add_book(b1)#to add new books
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(b4)
    lib.add_book(b5)

    s1 = StudentMember("Prathamesh jadhav") 
    f1 = FacultyMember("Mr.Santosh kadam")
    s2 = StudentMember("Pratik Ajagekar")
    
    
    lib.show_available_books() #list of books before borrowing
    
    s1.borrow_book(b1)   #list with borrow and return of book
    f1.borrow_book(b2)
    s1.borrow_book(b1) 
    s1.return_book(b1)
    s2.borrow_book(b1)
    
    lib.show_available_books()  #list of book after borrowed and returned by student and faculty
