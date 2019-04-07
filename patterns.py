######## 1. To print Floyyd's triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# def floyds_triangle(rows):
#     num = 1
#     for i in range(rows):
#         for j in range(i+1):
#             print(num,end = " ")
#             num += 1
#         print()
#
# no_of_rows = int(input("Enter the nummber of rows : "))
# floyds_triangle(no_of_rows)


############### 2. Left alligned Staircase problem
# *
# **
# ***
# ****

# height = int(input("Enter height of the staircase :"))
# for i in range(1, height+1):
#     print("*" * i)   # for left allignment

############### 3. Right alligned Staircase problem
   # *
  # **
 # ***
# ****

# height = int(input("Enter height of the staircase :"))
# for i in range(1, height + 1):
#     print(" " * (height - i),"*" * i )    # For Right allignment

############### 4. Inverted Left Alligned staircase
# Enter rows of Triangle :4
# * * * *
# * * *
# * *
# *

# rows = int(input("Enter rows of Triangle :"))
# for i in range(rows,0,-1):
#     print("* " * i)

############### 5. Inverted Pyramid problem. Hint Repeat "* ". Add spaces in each row as row-i
# Enter rows of Pyramid :3
# * * *
#  * *
#   *

# rows = int(input("Enter rows of Pyramid :"))
# for i in range(rows, 0, -1):
#     space = rows -i
#     print((" " * space) + ("* " * i))

############### 6. Pyramid problem.
   # *
  # * *
 # * * *
# * * * *
#
# rows = int(input("Enter rows of Pyramid :"))
# for i in range(1,rows+1):
#     space = rows -i
#     print((" " * space) + ("* " * i))

############### 6. print diamond with a breadth.
   # *
  # * *
 # * * *
# * * * *
#  * * *
#   * *
#    *

# rows = int(input("Enter rows of Pyramid :"))
# for i in range(1,rows+1):
#     space1 = rows-i             # space to be insterted in every row is rows-i
#     print((" " * space1) + ("* " * i))
# for j in range(rows-1,0,-1):    # Starting value is reduced as there is no need to repeat central line
#     space2 = rows-j
#     print((" " * space2) + ("* " * j))


############### 7. print Half diamond with a breadth (Right alligned). Same as problem 6, just remove space in "*"
   # *
  # **
 # ***
# ****
#  ***
#   **
#    *

# rows = int(input("Enter rows of Pyramid :"))
# for i in range(1,rows+1):
#     space1 = rows-i             # space to be insterted in every row is rows-i
#     print((" " * space1) + ("*" * i))
# for j in range(rows-1,0,-1):    # Starting value is reduced as there is no need to repeat central line
#     space2 = rows-j
#     print((" " * space2) + ("*" * j))

############### 8. print Half diamond with a breadth (Left alligned). Same as problem 6, just remove space in "*"

# *
# * *
# * * *
# * *
# *

# rows = int(input("Enter rows of Pyramid :"))
# for i in range(1,rows+1):
#     print("* " * i)
# for j in range(rows-1,0,-1):    # Starting value is reduced as there is no need to repeat central line
#     print("* " * j)

############### 9. print Floyds triangle of alphabets - Left alligned alphabets.
# A
# B C
# D E F
# G H I J

# def floyds_triangle_alphabets(rows):
#     num = 65
#     for i in range(rows):
#         for j in range(i+1):
#             print(chr(num),end = " ")
#             num += 1
#         print()
#
# no_of_rows = int(input("Enter the number of rows : "))
# floyds_triangle_alphabets(no_of_rows)

############### 10. print triangle of alphabets. Same as 6

# def triangle_alphabets(rows):
#     num = 65
#     for i in range(rows):
#         for j in range(1,i+2):
#             space1 = rows - i
#             if j == 1:
#                 print((" " * space1),chr(num),end=" ")
#             else:
#                 print(chr(num), end=" ")
#             num += 1
#         print()

# rows = int(input("Enter rows of Pyramid :"))
# triangle_alphabets(rows)


