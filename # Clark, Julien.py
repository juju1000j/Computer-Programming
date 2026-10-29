# Clark, Julien
# Computer Programming, period 4
# Assignment: Homework 4a
# Date: 10/26


peopleiknow = {"First Name": "Julien", "Last Name": "Clark", "Age": 17, "City": "Los Angeles"}

for thing, v in peopleiknow.items():
    print (thing)
    print (v)

aboutme = {"name": "Julien Clark", "age": 17, "favFood": "Bahn Mi", "hairColor": "Brown", "favSubject": "Astronomy", "favSweet": "Snickers", "favHobbies": "Sculpting", "likeCoding": False}

print (aboutme)

phonebook = {
"John" : 938477566,
"Jack" : 938377264,
"Jill": 947662781}

phonebook["Jake"] = 938273443

#phonebook.remove["Jake"]

#testing if this successfully removes phonebook["Jake"]

print (phonebook)

#did not work


del phonebook["Jake"]

print (phonebook)

del phonebook["Jill"]

print (phonebook)

glossary = {"ubiquitous": "ever-present, abundant, common", "gallant": "brave, fierce, loyal", "histrionic": "theatrical, hysterical, dramatic", "renal": "of or relating to the kidneys", "triumph": "victory, win, conquer, succeed"}
#this is for part 1 of the problem

#now onto "glossary 2"

for k in glossary.keys():
    print (k)

#running loop
#the loop works, i will now add 5 more terms to the glossary.

glossary.update({"erupt": "explode, burst, release", "hill": "geological formation that is elevated more than the terrain surrounding it but not high enough to be considered a mountain", "energy drink": "beverage containing large amounts of caffeine sold to consumers", "magic": "that which does not have a naturalistic explanation", "kaleidoscope": "optical toy or instrument containing colored glass and mirros that create changing symmetrical patterns when rotated"})

# running the program again, this time with items

for k, v in glossary.items():
    print (k)
    print (v)

# the terms were successfully added

# now onto rivers

rivers = {"Yangtze River": "China","Yellow River":"China","Mississippi River":"United States of America"}


for k, v in rivers.items():
    print(f"{k} runs through {v}")

# i used a loop to print both the name of the river and the country

person1 = {"first name":"Jimmy",
           "last name" :"McGill",
           "fav_color": "White",
           "birth month": "February"}
person2 = {"first name":"Chuck",
           "last name": "McGill",
           "fav_color": "Blue",
           "birth month": "December"}
person3 = {"first name":"Don",
           "last name": "Draper",
           "fav_color": "Turquoise",
           "birth month": "April"}

#now for cities or nesting 2

Nesting_2 = {"Dodge City": [{"country":"the united states", "population":"27,653","fun fact": "this city is the origin of the expression 'we better get the heck out of dodge'"}],"Los Angeles":[{"country": "the united states of america", "population":"3.87 million", "fun fact": "Los Angeles means the angels in english when translated from spanish"}], "luckenbach": [{"country": "the united states", "population": "3","fun fact": "its name comes from an 1886 love story"}]}

for k,v in Nesting_2.items():

    print (k)
    print (v)


