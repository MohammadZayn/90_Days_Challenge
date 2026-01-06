# Find the 2nd largest number
nums = [1,2,3,6,19,26,45,23,78,11,52,77,22,89,32,98]

#1
nums.sort()
print(f"The original list after sorted:{nums}")
print(nums[-2])

#2
nums.sort(reverse=True)
print(f"The reversed list after sorted:{nums}")
print(nums[1])


#Reverse a list without using reverse()
n = [1,2,3,6,19,26,45,23,78,11,52,77,22,89,32,98]
#1
l=[]
for x in n:
    l.insert(0,x)
print(l)

#2
print(n[::-1])
