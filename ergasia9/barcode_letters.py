import string
from collections import Counter 
#import two libraries common string operations and counter in collections
chars = string.ascii_letters

app = []
stars = []
final = []

with open("letters.txt","r") as f:

    lines = f.readlines()
    for line in lines:
        for char in chars:
            if ord(char) % 2 == 1: # checks if the character in ascii_letters is prime 
                for letter in line:
                    if char == letter:
                        app.append(char)
                       
# creating a dictionary that counts the frequency of occurrence of ascii_letters in upper case
a = dict(Counter([x.upper() for x in app]))

# built-in function that returns a new list containing the upper case letters in ascending order
# In this case the list a is being sorted and filled every time with the special character *
for key in sorted(a):
    ast = '*' * a[key] # variable that counts the letters with the special character *
    for star in ast:
        stars.append(star)
    print(key+": "+ str(stars))
    stars.clear() 
# print the total amount of the special character * in numbers
print([a[key] for key in sorted(a)])