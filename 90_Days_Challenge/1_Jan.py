#Replace spaces in a string with %20
#1
m = "He is a good boy but not as much as good we can trust him"
new = ""
for x in m:
    if x ==" ":
        new = new + "%20"
    else:
        new = new + x
print(new)

#2
print(m.replace(" ","%20"))

#Count words in a sentence
#1
sentence = "He is a good boy but not as much as good we can trust him"
l = set(sentence)
new = [f"{word}:{sentence.count(word.lower())}" for word in l]
print(new)

#2
Counts ={}
for x in sentence:
    count = Counts.get(x,0)+1
    Counts[x] = count
print(Counts)