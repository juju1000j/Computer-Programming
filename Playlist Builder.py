# Julien Clark
# 
# playlist with 4 songs
playlist = ["life is a highway", "triohatala - stimmhorn", "let it be", "bible in chinese 2x speed"]



# userinput for new song
new_song = input (f"add one more song here: ")

# cleaning new song
new_song.strip()
new_song.title()

# append new song
playlist.append(new_song)
# using len() to print how many songs are on the playlist
print (len(playlist))
# defined bonus song
bonus_song = "stairway to heaven"
playlist.insert(0, bonus_song)
# inserted bonus song
playlist.remove("life is a highway")
del playlist[1]
print(sorted(playlist))

print(playlist.sort())

playlist.sort()
# reversed playlist in alpha order
playlist.reverse()

print("photograph" in playlist)

for song in playlist: 
    print (song)

for song in playlist:
    print (song.upper())

for i in range(len(playlist)):
    print (i+1, playlist[i])

#modification of the part 4 for loop

for i in range(len(playlist)):
    if "b" in playlist[i]:
            print (i+1, playlist[i]) 

    