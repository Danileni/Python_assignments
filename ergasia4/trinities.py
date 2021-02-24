import re
import random
#import two libraries regular expression operations and generator pseudo-random numbers 
words = []
filtered_words = []

with open("two_cities.txt", "r",encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        sentence = line.split(" ") #built-in method that splits the lines with whitespace
        for word in sentence:
            # built-in method that removes any trailing characters (characters at the end a string), 
            # space is the default trailing character to remove.
            # In this case every special character that is not whitespace is being stored in a
            # list of words.
            if word.rstrip() != "": 
                words.append(word.rstrip())

for word in words:
    filtered_word = re.sub('[^A-Za-z0-9]+', '', word) 
    # built-in method which does regex substitution meaning that removes 
    # all special characters, punctuation and spaces from word 
    # in order to have only letters and numbers.
    if filtered_word != "" :
        filtered_words.append(filtered_word)

# taking the triplets from the filtered_word list
triplets = [filtered_words[i:i + 3] for i in range(0, len(filtered_words), 3)]

# if it's not a triplet then is is being removed from the list
for triplet in triplets:
    if len(triplet) != 3:
        triplets.pop()

indexes = []
counter = 0 # counter that counts the words
# open a file to write the random text that is being produced by the triplets
file = open("final.txt", "w")

print("[*] Searching for matching triplets please wait...\n")

for i in range(len(triplets)):
    
    indexes.clear()
    # taking the two last words from the triplet
    random_index = random.randint(0, len(triplets)-1)
    word1 = triplets[random_index][1]
    word2 = triplets[random_index][2]
    # stores the two last words from the triplet in indexes list that every time is being cleared
    for trio in triplets:
        if trio[0] == word1 and trio[1] == word2:
            indexes.append(triplets.index(trio))
    
    if len(indexes) > 0  and counter < 200:
        # taking random triplets and write them with whitespace in the final file 
        rand_match = random.choice(indexes)
        file.write(" ".join(triplets[rand_match]) + " ")
        counter += 1
    elif counter == 200:
        print("[*] Successfully created the final file.")
        break