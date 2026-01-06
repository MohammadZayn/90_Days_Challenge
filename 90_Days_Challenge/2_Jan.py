#Check if a string contains only digits
#1
dig_str = "M123ohammad Shai123k"
for x in dig_str:
    if x.isdigit():
        print(f'this string has a digit..{x}')
        break
#2
for x in dig_str:
    if x in "1234567890":
        print(f'this string has a digit..{x}')

#Capitalize the first letter of each word
#1
sen = "mohammad is a very bad batsman he did not helped team to win in any situation"
new_list =[x.capitalize() for x in sen.split(" ")]
print(" ".join(new_list))