

"""
Generate a random interger 1-20 based on the number chosen at random, check  to see if it falls between certain ranges

if # > 15 result will be "Cherries"
otherwise > 10, result = "Orange"
otherwise > 5, result = "Plum"
otherwise > 2, result = "Melon"
otherwise > 1, result = "Bell"
if the # is none of the above, result = "Bar"

iterate using a loop three times and print the results to the user 

"""

"""
num = generate random number

if num > 15 then the result = "Cherries"

otherwise if num is > 10,
    then result = "Orange"
otherwise if num is > 5, 
    then result = "Plum"
otherwise if num is > 2, 
    then result = "Melon"
otherwise if num is > 1, 
    then result = "Bell"
if num != any number above, 
    then result = "Bar"

loop three times
    print the output (fruit) to the user

"""

import random

def main():
    for i in range(0, 3):
        spin()

def spin():
    rand_num = random.randint(1, 20)
    output = ""

    if(rand_num > 15):
        output = "Cherries"
    elif(rand_num > 10):
        output = "Orange"
    elif(rand_num > 5):
        output = "Plum"
    elif(rand_num > 2):
        output = "Melon"
    elif(rand_num > 1):
        output = "Bell"
    else:
        output = "Bar"

    print("Your number is: ", rand_num , "and the corresponding result is",  output,)
    

main()