# Find the longest word in a sentence
#1
sent = "I am learning Python programming language"
extract = sent.split(" ")
x =0
word=""
for i in extract:
    if len(i)>=x:
        x=len(i)
        word = i
print(f"the longest word is {word} and it has a length of {x}")

# Count the anagrams of a list and separate them by length wise
anagrams = ["eat","tea","at","ta","bat","tan","ate","nat"]
new_list = []
for word in anagrams:
    new = [oword for oword in anagrams if sorted(word) == sorted(oword)]
    if new not in new_list:
        new_list.append(new)
print(new_list)
