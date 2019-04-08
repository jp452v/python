

list_of_books = [{'name': 'The bible', 'price':'0.99','ISBN':'1111111'}]


def add_a_book(name,price,ISBN):
    list_of_books.append({'name': name, 'price':price, 'ISBN':ISBN})
    return list_of_books


def delete_a_book(ISBN):
    for each_book in list_of_books:
        if 'ISBN' in each_book.values():
            list_of_books.remove(each_book)
    return list_of_books




list1 = add_a_book('bible2','1.99','222222')
# list2 = add_a_book('bible2','2.99','333333')
print(list1)

x = delete_a_book('1111111')
print('deleted one',x)


# Add a validation, if book already exists raise an exception and say it already exists. Check with ISBN, raise exception

