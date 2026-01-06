# Find the largest and smallest element in a list
s_l=[-1,18,99,100,121,-8,-3,22]

#1
print(max(s_l),min(s_l))

#2
current_num =s_l[0]
for num in s_l:
    if num >= current_num:
        current_num=num
print(current_num)
low_num =s_l[0]
for num in s_l:
    if num <= current_num:
        low_num=num
print(low_num)

# Remove duplicates from a list
d_l = [1,2,5,7,9,3,4,6,9,2,4,6,92,6,8,3,7,8,3,67,8,3,7,8,]

#1
print(set(d_l))

#2
m=[]
comp = [m.append(val) for val in d_l if val not in m]
print(m)