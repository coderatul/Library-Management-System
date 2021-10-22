# function to delete Book code
def del_code(n):
    a_file = open("Book_code.txt", "r+")
    lines = a_file.readlines()
    k = lines[n]
    lines.remove(k)
    lines_del = open("Book_code.txt", "w")
    lines_del.writelines("")
    app_lines = open("Book_code.txt", "a")
    app_lines.writelines(lines)
    a_file.close()
    lines_del.close()
    app_lines.close()

# function to delete books
def del_book(n):
    a_file = open("Books.txt", "r+")
    lines = a_file.readlines()
    k = lines[n]
    lines.remove(k)
    lines_del = open("Books.txt", "w")
    lines_del.writelines("")
    app_lines = open("Books.txt", "a")
    app_lines.writelines(lines)
    a_file.close()
    lines_del.close()
    app_lines.close()

# function to delete Author name
def del_Auth_name(n):
    a_file = open("Author_name.txt", "r+")
    lines = a_file.readlines()
    k = lines[n]
    lines.remove(k)
    lines_del = open("Author_name.txt", "w")
    lines_del.writelines("")
    app_lines = open("Author_name.txt", "a")
    app_lines.writelines(lines)
    a_file.close()
    lines_del.close()
    app_lines.close()


# function to delete Publication year 
def del_pub_year(n):
    a_file = open("Publish_year.txt", "r+")
    lines = a_file.readlines()
    k = lines[n]
    lines.remove(k)
    lines_del = open("Publish_year.txt", "w")
    lines_del.writelines("")
    app_lines = open("Publish_year.txt", "a")
    app_lines.writelines(lines)
    a_file.close()
    lines_del.close()
    app_lines.close()
