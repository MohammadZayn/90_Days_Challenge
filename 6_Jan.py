# Sort a list without using sort()
data = [5, 2, 9, 1, 5, 6]
m = data.sort()






# Count occurrences of each element in a list

da = [5, 2, 9, 1, 5, 6]
l ={}
for x in da:
    m =l.get(x,0)+1
    l[x]=m
print(l)