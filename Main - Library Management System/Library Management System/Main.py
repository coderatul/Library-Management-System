import pyfiglet     # importing pyfiglet module to print header
import datetime     # importing datetime module to print present date and time
import random       # importing random module to print random quotes at the exit of the program
from prettytable import PrettyTable  # importing prettytable module to create table
import BookDetails as bd   # importing BookDetails module which have been created
import DeleteBook as db   # importing DeleteBook module which have been created
import AddBook as ab   # importing AddBook module which have been created


# printing header using the pyfiglet module
Header = pyfiglet.figlet_format("Welcome to AB Library", font = "digital")
print(Header)
print("-"*133)

# printing Date and Time using the datetime module
date = datetime.datetime.now()
print("Present Date and Time is", date)

print("-"*133)

# creating a list of books from a text file to add or delete from it
Books = bd.name_book()
# print(Books)

# creating a list of book codes
book_num_1 = bd.code_book()

# creating a list of Author names
Auth = bd.auth_book()


# creatind a list of publish year
pub_year = bd.pub_book()

def createTable():
    A = len(Books)
    # using prettytable module to create the table
    menu = PrettyTable(["Book code","Name of the Books","Author's Name","Publish Year"])
    for i in range(A):
        menu.add_rows([
            [book_num_1[i],Books[i],Auth[i],pub_year[i]],
        ])
    return menu
menu = createTable()




def Add_book(): # Creating a Function to Add a Book to the Library
    # asking user to enter a book they want to add to the library
    name = input("Enter a book you want to add to the library : ")
    if name in Books:  # if book already in the library
        # leaving a message to the user that the book already in the library
        print("The book you wanted to add already exist in the library!")

    else:
        book_num = input("Enter the Book Code : ")  # asking the user to enter the book code to add to the book details
        pub_year_1 = input("Enter the publish year of the book : ")  # asking the user to enter the publish year
        auth_1 = input("Enter the Name of the Author of the book : ")  # asking the user to enter the name of the author

        # adding the book to the library
        ab.add_book(name)
        ab.add_auth(auth_1)
        ab.add_code(book_num)
        ab.add_pub_year(pub_year_1)

        # adding all the entered details of the books by the user to the table
        menu.add_rows([
            [book_num, name, auth_1, pub_year_1]
        ])
        Books.append(name)
        book_num_1.append(book_num)
        Auth.append(auth_1)
        pub_year.append(pub_year_1)
        print("The book has been added to the library!")





def del_book(): # Creating a Function to delete a book from the library
    # asking user to enter a book they want to delete from the library
    row_n = str(input("Enter the code number of the book you want to delete from the library : "))
    if row_n in book_num_1:
        r = book_num_1.index(row_n)
        db.del_code(r)
        db.del_book(r)
        db.del_pub_year(r)
        db.del_Auth_name(r)
        menu.del_row(r)

        book_num_1.remove(row_n)
        Books.pop(r)
        pub_year.pop(r)
        Auth.pop(r)
        print("The Book has been Successfully Deleted!")


    else:
        # if the book is not there in the library it prints the following statement
        print("The book you are trying to delete is not in the library!")


def exit_prog(): # Creating a Function to Print a Quote while exiting
    # printing random quotes using random module
    print(random.choice(["'Nothing is pleasanter than exploring a library'",
                         "'To add a library to a house is to give that house a soul'",
                         "'No furniture so charming as books'"]))
    # printing Thank you message to the user
    print("Thank You for Visiting our Library! Visit us again.")
    # break  # Exiting the program


while True:
    print("-"*38,"PLEASE CHOOSE ANY OF THE OPTIONS GIVEN BELOW TO PROCEED","-"*38)
    # creating the list of options to choose to proceed further
    print("""1. Display all the available books available in the library
2. Add a book to the library
3. Delete a book from the library
4. Exit""")
# asking user to choose a option from above
    options = input("Enter your option : ")

    if options == '1':
        print(menu) # if the option is 1 it prints the table
    elif options == '2':
        Add_book()
    elif options == '3':
        del_book()
    elif options == '4':
        exit_prog()
        break  # Exiting the program
    else:
        # if user chooses none of the option given above
        print("Please choose the appropriate option")
        # printing the message showing user to choose correct options

