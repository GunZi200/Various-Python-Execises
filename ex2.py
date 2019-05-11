# Write a function to check whether a list contains a particular element.
# LAUSN:
A = [1,2,3,4,5,6] # random 1x5 fylki

def myFunction(x,y):
    for i in x:
        if (i == y):
            return print(True)
    return print(False)

myFunction(A,9)


