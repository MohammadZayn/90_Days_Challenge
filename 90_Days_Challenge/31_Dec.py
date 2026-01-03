#Convert string "1234" to integer without using int()
str_number ="8019455881"
int_value = 0
for x in str_number:
    a=ord(x)
    b=ord("0")
    num = a-b
    int_value= int_value*10+num
print(int_value)

#Print duplicate characters in a string
m='mohammad shaik'
#1
print(set(m))

#2
r_d =""
for x in m:
    if x not in r_d:
        r_d += x
print(r_d)