#function to add Book code
def add_code(p):
    n = open("Book_code.txt", "a")
    n.write(p+"\n")
    n.close()

#function to add Book name
def add_book(p):
    n = open("Books.txt", "a")
    n.write(p+"\n")
    n.close()

#function to add publish year 
def add_pub_year(p):
    n = open("Publish_year.txt", "a")
    n.write(p+"\n")
    n.close()

#function to add Author name
def add_auth(p):
    n = open("Author_name.txt", "a")
    n.write(p+"\n")
    n.close()
