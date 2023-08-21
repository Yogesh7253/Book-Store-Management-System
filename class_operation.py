from class_book import *

class Operation:
    booklist = []

    def addbook(self):
        ID = int(input("Enter Book ID : "))
        name = input("Enter the name of book : ")
        edition = int(input("Enter edition of book : "))
        publisher = input("Enter name of publisher : ")
        price = float(input("Enter price of book : "))

        book_obj = Book(ID,name,edition,publisher,price)
        self.booklist.append(book_obj)
        print("Book Added Successfully.")


    def view(self):
        for view in self.booklist:
            print(view,"\n")

    def delete(self):
        ID = int(input("Enter the ID of book you want to delete : "))
        for book in self.booklist:
            if ID == book.get_ID():
                self.booklist.remove(book)
                print("Book Successfully Deleted.")
                break
            else:
                print("Book not found.")

    def searchbookbyID(self):
        ID = int(input("Enter ID of the book you want to search : "))
        for search in self.booklist:
            if search.get_ID() == ID:
                print(search)
                break
        else:
            print("Book Not Found.") 

    def searchbookbyname(self):
        name = input("Enter name of the book you want to search : ")
        for search in self.booklist:
            if search.get_name() == name:
                print(search)
                break
        else:
            print("Book Not Found.")

    def update(self):
        ID = int(input("Enter the ID of the book you want to update : "))
        for updated in self.booklist:
            if updated.get_ID() == ID:
                name = input("Enter the name of book : ")
                edition = int(input("Enter edition of book : "))
                publisher = input("Enter name of publisher : ")
                price = float(input("Enter price of book : "))
                
                updated.set_name(name)
                updated.set_edition(edition)
                updated.set_publisher(publisher)
                updated.set_price(price)

            else:
                print("Book Not Found.")

    
                





