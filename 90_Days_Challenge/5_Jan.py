# Find missing number from a sequence
from jinja2.utils import missing

lon = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]

num =1
missing_num =[]
for x in range(max(lon)):
    if num not in lon:
        missing_num.append(num)
        num=num+1
    else:
        num =num+1
print(missing_num)

# Find common elements between two lists
a = [1, 2, 3, 4, 5, 5]
b = [3, 4, 5, 6]

#1
print(set(a).intersection(b))

#2
for x in range(len(a)):
    if a[x] in b:
        print(a[x],end=",")

