# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.


l=list(map(int,input("Enter the list elements:").split(" ")))
ele= int(input("Enter the number:"))
for i in range(0,len(l)):
    if(l[i]<ele):
        print(l[i],end=" ")

# Output:
# Enter the list elements:12 13 2 3 4 5
# Enter the number:5
# 2 3 4 