#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
def remove_dup_set(input_list):
    return list(set(input_list))

a = input("Enter the list elements1:").split(" ")

print(remove_dup_set(a))

# output:
# Enter the list elements1:1 12 21 1 12 3 4 4 5 6 5
# ['5', '6', '1', '12', '21', '3', '4']