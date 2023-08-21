from class_operation import *

class Main:
    def execute(self,choice,operation):
        if choice == 1:
            print("********** VIEW BOOKS *********")
            operation.view()
        if choice == 2:
            print("********* ADD BOOKS *********")
            operation.addbook()
        if choice == 3:
            print("*********** DELETE BOOKS **********")
            operation.delete()
        if choice == 4:
            print("********* SEARCH BOOKS BY ID ********")
            operation.searchbookbyID()
        if choice == 5:
            print("******** SEARCH BOOK BY NAME *********")
            operation.searchbookbyname()
        if choice == 6:
            print("*********UPDATE DETAILS ***********")
            operation.update()
        

operation = Operation()
main = Main()
while True:
    choice = int(input("1. View Books\n2. Add Books\n3. Delete Books\n4. Search Books By ID\n5. Search Books by Name\n6. Update Details\n Enter your choice :"))
    main.execute(choice,operation)


