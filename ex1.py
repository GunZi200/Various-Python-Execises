#OBJECTIVE: Create function which converts int to str and str to int.

# turns string into an integer.
def to_int(x): 
    return int(x)

# turns integer into a string.
def to_string(x):
    return str(x)

myInt = type(to_int("8"))
myString = type(to_string(8))

#þrjár leiðir til að prenta út. three ways to print the results.
print("to_int: {}".format(myInt))
print("to_string: {}".format(myString))

print("to_int: %s" %(myInt))
print("to_string: %s" %(myString))

# f-string: Python 3.6 and later
print(f'to_int: {myInt}.')
print(f'to_string: {myString}.')
