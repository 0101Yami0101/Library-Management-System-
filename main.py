# Basic Student Library Management System with OOPS

class Library:  

    def __init__(self,ListOfBooks):   #Constructor
        self.Books = ListOfBooks   #making the list to self.Books

    def DisplayAvailableBooks(self):  #method to display the books from the [ListOfBooks] list
        print("Books present in the list are\n")
        for a in self.Books:   #Loop to print the books in the list
            print("  " + a)

    def BorrowBook(self, bookName):
        if bookName in self.Books:   #If book is present in the list
            print(f"You have been issued the book {bookName}. Thanks")
            self.Books.remove(bookName) #Book name will be removed from the list
            return True
        else:
            print("The book has already been borrowed by someone else or the book is not available.")
            return False

    def ReturnBook(self,bookName):
        self.Books.append(bookName)  #Name will be added/Appended to the self.Book list
        print("Thanks for returning the book. Have a great day!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return or add: ")
        return self.book
    

if __name__ == "__main__":
    #Object Instantiation
    MainLib = Library(["Python","Django","MatLab","C++","Java"])

    #Display method 
    # MainLib.DisplayAvailableBooks()  #Try

    #BorrowBook method
    # MainLib.BorrowBook("Django")  #Try

    #Return Book method
    # MainLib.ReturnBook("C")  #Try

    Stu1 = Student()
    
    #menu

    while(True):
        Welcome = '''\n ++++..........Welcome to the Main Library............++++\n
        1. Display Books In Library
        2. Borrow A Book
        3. Add or Return A Book
        4. Exit Library'''
        a = int(input("Enter a choice: "))
        print(Welcome)

        if a == 1:
            MainLib.DisplayAvailableBooks()
        elif a == 2:
            MainLib.BorrowBook(Stu1.requestBook())
        elif a == 3:
            MainLib.ReturnBook(Stu1.returnBook())
        elif a == 4:
            print("Thanks for Visiting")
            exit()
        else:
            print("Invalid input")
    
    
    
