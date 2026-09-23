# Clark, Julien
# Computer Programming, period 4
# Assignment: Homework 3
# 9/10/2026

Hobbies = ("underwater basket weaving", "playing piano", "doing the wordle", "researching topics", "watching tech reviews")

print (Hobbies)

print (len (Hobbies))

print (Hobbies[2])

print (Hobbies[0])

listA = ["Hello"*100]

list1 = ["pumpkin", "halloween", "jack-o-lantern", "spooky"]

list2 = ["christmas", "new year", "holiday", "santa"]

list3 = [list1 + list2]

print (list3)

favFoods = ["sandwich", "pasta", "steak", "icecream", "burger"]

print (len (favFoods))

print (favFoods[2])

print (favFoods[-4])

favFoods.append("Julien")

favFoods.insert(2, "17")

favFoods.remove("burger")

print (favFoods)

i=1

for i in range(1, 20 +1): print(i)

for i in range (1, 20+1, 2): print(i)

animals = ["cat", "bumblebee", "tarantula"]
print (animals)
for thing in animals:
    print (f"a {thing} is fluffy")

print ("all of these animals are fluffy")

guestList = ["Albert Einstein", "Richard Feynman", "Enrico Fermi", "Dingly Dingusberg"]

for thing in guestList:
    print(f"Dear {thing}, you are invited to dinner at 123 Street St. in City City at 12:00 PM on January 1st, 2000")

# oh no Dingly couldn't make it
print (f"Unfortunately, {guestList[3]} can't make it.")

guestList.remove("Dingly Dingusberg")
guestList.append("Isaac Newton")
for thing in guestList:
    print(f"Dear {thing}, you are invited to dinner at 123 Street St. in City City at 12:00 PM on January 1st, 2000")


