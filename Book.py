########## Book Module
# name, price, ISBN
# Add a book
# Delete a book
# Replace book
# update book name
# update book price
# get a book
# get all books


list_of_books = [{'name': 'Telugu bible', 'price':'0.99','ISBN':'1111111'}]
print("Initial list of books :\n", list_of_books)


def goto_menu():
    flag = True
    ch = input('\nDo you want to go to Main menu (Y/N)? ')
    if ch.capitalize() != "Y":
        flag = False
    return flag

def add_a_book(name,price,ISBN):
    list_of_books.append({'name': name, 'price':price, 'ISBN':ISBN})
    return list_of_books


def delete_a_book(ISBN):
    for each_book in list_of_books:
        if ISBN in each_book.values():
            list_of_books.remove(each_book)
    return list_of_books




################## Main loop ######################


while goto_menu():
    print('\n########## Main Menu ###########')
    print('1) Add Book(s)')
    print('2) Delete book(s)')
    print('3) Replace a book')
    print('4) Update a book name')
    print('5) Update a book price')
    print('6) Update a book ISBN code')
    print('Q) Quit the program')
    print('########################################')
    menu_choice = input("\n\nPlease select assignment number (1 - 6) or Q to quit: ")
    if menu_choice == '1':
        ### Add book to list_of_books
        num_of_books = int(input("How many number of books you would like to add ?"))
        for each_book in range(num_of_books):
            bk_name = input("Enter book name")
            bk_price = input("Enter Price of the book")
            bk_isbn = input("Enter ISBN code of teh book")
            add_a_book(bk_name, bk_price, bk_isbn)
        print("List of books after addition :\n", list_of_books)
    elif menu_choice == '2':
        ### Delete book from list_of_books
        num_of_books = int(input("How many number of books you would like to delete ?"))
        for each_book in range(num_of_books):
            bk_isbn = input("Enter ISBN code of the book to delete")
            delete_a_book(bk_isbn)
        print("List of books after deleting :\n", list_of_books)
    elif menu_choice.capitalize() == "Q":
        print('Bye, See you later!')
        break
    else:
        c = input('OOPS! Invalid Input!! Do you want to try again? (Y/N) :')
        if c.capitalize() == "Y":
            continue
        else: break








#### Delete a book
# book_isbn = input("Enter ISBN of the book to be deleted")
# delete_a_book(book_isbn)
# print("After deleting a book, list of books",list_of_books)



# Add a validation, if book already exists raise an exception and say it already exists. Check with ISBN, raise exception

