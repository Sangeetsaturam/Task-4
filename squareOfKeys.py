#Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)    
printDict()

# Output:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 
# 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}