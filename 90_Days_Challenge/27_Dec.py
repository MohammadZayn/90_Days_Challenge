# Count the anagrams of a list and separate them by length wise

anagrams = ["eat","tea","at","ta","bat","tan","ate","nat"]
new_list = []
for word in anagrams:
    new = [oword for oword in anagrams if sorted(word) == sorted(oword)]
    if new not in new_list:
        new_list.append(new)
print(new_list)

# Reverse a string without using built-in reverse functions
#1
string = "Mohammad is a bad boy"
print("".join(reversed(string)))

#2
rev_string = ""
for x in string:
    rev_string = x+rev_string
print(rev_string)

#3
print(string[::-1])

# Check if a string is a palindrome
name = "A man, a plan, a canal – Panama"
clean_name=""
for x in name:
    if x.isalpha()== True:
        clean_name=clean_name+x
rev_name = clean_name[::-1]
y=0
for x in clean_name:
    a =rev_name[y].lower()
    b=x.lower()
    if a==b:
        y+=1
    else:
        print('Not palindorme')

# Count frequency of each character in a string
#1
st = "Mohammad is a bad boy but he doesn't look like a bad boy I would say he a bad and good guy"
d = {}
for x in st:
    val=x.lower()
    if val not in d:
        d[val] = 1
    else:
        d[val] += 1
print(d)

#2
co={}
for x in st:
    val = x.lower()
    m=co.get(val,0)+1
    co[val] =m
print(co)

#3
e = {}
for x in st:
    al = x.lower()
    num = st.count(al)
    e[al]=num
print(e)