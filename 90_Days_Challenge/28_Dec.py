# Remove duplicate characters from a string
#1
from Social_Media.Facebook_Messenger import count

name = "Mohammad"
remove_duplicates_string = ""
for character in name:
    char = character.lower()
    if char not in remove_duplicates_string:
        remove_duplicates_string += character
print(remove_duplicates_string)

#2
print(set(name))

#3
empty ={}
num = 1
for x in name:
    chr = x.lower()
    if chr not in empty.values():
        empty[num]=x
        num=num+1
print(empty)

#Find the first non-repeating character

s = "aabbccddeffghhiijjkkllmmnnxopqqrrsstt"
non_repeated_characters = ""
for character in s:
    if s.count(character)<=1:
        non_repeated_characters += character
print(non_repeated_characters)
