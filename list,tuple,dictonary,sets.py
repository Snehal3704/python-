'''
lists are changable 
user input values stroing in string


nums = input("Enter the numbers with a space in between\n")

print(nums)

num_list=nums.split(" ")

#num_list= list(map(lambda x: int(x), num_list))

num_list= list(map(lambda x :int(x), num_list))

# i=0
# while i <len(num_list)
#     num_list[i]=int(num_list[i])
#     i+=1

print(num_list)

list comprehension

sum =0
new_list =[ x for x in range(10) if x%2 ==1 ]
print(new_list)

for loops in list
a=[0,5,8,2,4,3,9]
for element in a:
    print(element**2)

'''

'''
functions in python 

**modules

import math as m
print(m.pi)
'''
from math import pi





