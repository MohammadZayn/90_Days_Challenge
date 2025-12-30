# Swap two variables without using a temporary variable
#1
a = 10
b = 20
a,b = b,a
print(a,b)

#2 tuple unpacking
T = (10,20)
a,b =T
print(a,b)
print(b,a)

# Count vowels and consonants in a string

H = 'aAeEiIoOuUbBccCddDEfFgGhHiIjJkKlLmMnNppPqrRstTuvVwWxyYZz'
vowels="aeiouAEIOU"
vowels_count=0
for val in vowels:
        if val in H:
            vowels_count +=1
consonant_count=len(H)-vowels_count
print(vowels_count,consonant_count)