# 7. Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
#  For practice, write this code inside a function.

a = input("Enter the list elements1:").split(" ")

def listend(x):
    return [x[0], x[-1]]

print(listend(a))

# output:
# Enter the list elements1:1 2 3 4 5 6 7
# ['1', '7']