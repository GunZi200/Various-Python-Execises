# http://www.snakify.org/en/lessons/print_input_numbers/problems/two_timestamps/
# A timestamp is three numbers: a number of hours, minutes and seconds. 
# Given two timestamps, calculate how many seconds is between them. 
# The moment of the first timestamp occurred before the moment of the second timestamp.

# Read an integer:
def readInt(): return int(input())
# Read a float:
def readFloat(): return float(input())

List = []
List.append(readInt()) 
List.append(readInt())
List.append(readInt())
List.append(readInt())
List.append(readInt())
List.append(readInt()) 
time = abs(List[0]-List[3])*3600 - (List[1]-List[4])*60 - (List[2]-List[5]) 
print(time)
