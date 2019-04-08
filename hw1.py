
############# Function declarations ##############

def compare_num():
    x = int(input("Give first number: "))
    y = int(input("Give second number: "))
    if x > y:
        print(x, "is greater than ",y)
    elif x < y:
        print(x, "is less than ", y)
    else: print(x, "is equal to ", y)


def descending_num():
    x = int(input("Give first number (Highest) : "))
    y = int(input("Give last number (Lowest) : "))
    while x >= y:
        print(x)
        x = x - 1


def ascending_num():
    y = int(input("Give first number (Lowest) : "))
    x = int(input("Give last number (Highest) :  "))
    while y <= x:
        print(y)
        y =  y + 1

def list_items_print():
    num = [1,2,3,4,5]
    print('Given list is: [1,2,3,4,5] ')
    print('The items in the given list are: ')
    for n in num:
        print(num[n-1])

def list_items_print_less_than():
    num = [1,2,3,4,5]
    print('Given list is: [1,2,3,4,5] ')
    print('The items in the given list < 4 are: ')
    for n in num:
        if num[n-1] < 4:
            print(num[n-1])

def list_items_print_except():
    num = [1,2,3,4,5]
    print('Given list is: [1,2,3,4,5] ')
    print('The items in the given except 4 are: ')
    for n in num:
        if num[n-1] != 4:
            print(num[n-1])


def list_manipulate():
    mylist = ["Seattle","LA","NY","CA"]
    print('Given list is                       : ["Seattle","LA","NY","CA"] ')
    print('The third item in the given list is :', mylist[2])
    mylist[1]="Boston"
    print('The 2nd item in the modified list   : ', mylist[1])
    print('The length of the given list is     : ', len(mylist))

def goto_menu():
    fl = True
    ch = input('\nDo you want to go to Assignment menu (Y/N)? ')
    if ch.capitalize() != "Y":
        fl = False
    return fl



################## Main loop ######################

flag = True
while goto_menu():
    print('\n########## Assignment Menu ###########')
    print('1) Compare given two numbers')
    print('2) Print descending numbers')
    print('3) Print ascending numbers')
    print('4) Print items in given list')
    print('5) Print only items in given list that are less than a number')
    print('6) Print items in given list except a number')
    print('7) Manipulate given list of items')
    print('Q) Quit the program')
    print('########################################')
    f = input("\n\nPlease select assignment number (1 - 7) or Q to quit: ")
    if f == '1':
        compare_num()
    elif f == '2':
        descending_num()
    elif f == '3':
        ascending_num()
    elif f == '4':
        list_items_print()
    elif f == '5':
        list_items_print_less_than()
    elif f == '6':
        list_items_print_except()
    elif f == '7':
        list_manipulate()
    elif f.capitalize() == "Q":
        print('Bye, See you later!')
        break
    else:
        c = input('OOPS! Invalid Input!! Do you want to try again? (Y/N) :')
        if c.capitalize() == "Y":
            continue
        else: break













##### Assignment 1: Comparison of two numbers ##
# flag = True
# while flag:
#     f = input("\nDo you want to continue, press Y / N? : ")
#     if f.capitalize() == "Y":
#        x = int(input("Give first number: "))
#        y = int(input("Give second number: "))
#        if x > y:
#            print(x, "is greater than ",y)
#        elif x < y:
#            print(x, "is less than ", y)
#        else: print(x, "is equal to ", y)
#     elif f.capitalize() == "N":
#         flag = False
#         print("\n\nBye, See you later!")
#     else: print("\n\nOOPS! Invalid Input!! Try again!!!")


## Assignment 2: Display 9,8,7,6,5,4,3,2,1 ##

# x = 9
# y = 1
# while x >= y:
#    print(x)
#    x = x - y

## Assignment 3: 1,2,3,4,5,6,7,8,9 ##

# x = 9
# y = 1
# while y <= x:
#    print(y)
#    y =  y + 1

## Assignment 4: Print items in list ###

# numbers = [1,2,3,4,5]
# for n in numbers:
#    print(numbers[n-1])

## Assignment 5 ###
# numbers = [1,2,3,4,5]
# for n in numbers:
#    if numbers[n-1] <= 4:
#        print(numbers[n-1])

## Assignment 6 ###

# numbers = [1,2,3,4,5]
# for n in numbers:
#    if numbers[n-1] != 4:
#        print(numbers[n-1])

## Assignment 7 ###
# mylist = ["Seattle","LA","NY","CA"]
# print(mylist[2])
# mylist[1]="Boston"
# print(mylist[1])
# print(len(mylist))

