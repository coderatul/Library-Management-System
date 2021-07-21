#creating a list of books from a text file to add or delete from it
def name_book():
    n = open("Books.txt", "r")
    n.seek(0)
    Books = []
    while True:
        r = n.readline()
        if len(r) == 0:
            break
        else:
            # r = n.readline()
            j = len(r)
            Books.append(r[:j - 1])
    return Books
    n.close()


#creating a list of book codes
def code_book():
    n = open("Book_code.txt", "r")
    n.seek(0)
    book_num_1 = []
    while True:
        r = n.readline()
        if len(r) == 0:
            break
        else:
            # r = n.readline()
            j = len(r)
            book_num_1.append(r[:j - 1])
    return book_num_1
    n.close()


#creating a list of Author names]
def auth_book():
    n = open("Author_name.txt", "r")
    n.seek(0)
    Auth = []
    while True:
        r = n.readline()
        if len(r) == 0:
            break
        else:
            # r = n.readline()
            j = len(r)
            Auth.append(r[:j - 1])
    return Auth
    n.close()


#creatind a list of publish year
def pub_book():
    n = open("Publish_year.txt", "r")
    n.seek(0)
    pub_year = []
    while True:
        r = n.readline()
        if len(r) == 0:
            break
        else:
            # r = n.readline()
            j = len(r)
            pub_year.append(r[:j - 1])
    return pub_year
    n.close()
