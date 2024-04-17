# # print("hello!")
# #age =20;
# # name='snehal'

# # print('age')    #to print as a string
# #print(age)      #to print the value of variable

# name='snehal banerjee'
# print(name,type(name))

# age=20
# print(age,type(age))

# year_of_birth=2004
# print(year_of_birth,type(year_of_birth))

# user = True
# print(user,type(user))

# fav_food=['apple','grapes','banana']        #list
# print(fav_food,type(fav_food))

'''

# a=5;
# b=3;
# print(5//3) # printing the remaing part 
# print(5**3) #printing it for power format
'''

'''
print('enter your name')
name=input()
print('your name is',name)
# input function always give string as output

'''
#**input function**

'''
a=int(input('enter no a:'))      #type casting string to int type
print(type(a))      #input fucntion always give str type as outtput

b=int(input('enter no b:'))
print('multiplication of a and b is :',a*b)

'''

'''
**RANGE FUCNTION IN PYTHON**

range gives a sequence upto a certain number
range(10) = generating numbers form 0 to 9 also we can generate using starting and ending index
x=range(10)
print(x)   == 0,1,2,3,4,5,6,7,8,9

but when using print('range(10)') = only show range(10)

**for printting in list format**

a=list(range(5,10,2)) # printing 2 gap
print(a)

'''

'''
**for loops in python**

print function already creatre a new line charecter after sucessfully iterating
but we can change it ex:

for x in range(10):    #printing squre values of numbers form 0 to 9
    print(x*x,end=', ') 
    output = 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 
    so we can modify it using end statement

using for we can iterate in the lists also
ex
a=['snehal','banerjee','gublu']

for x in a:    
    print(x*2,end=', ')     #output =snehalsnehal, banerjeebanerjee, gublugublu, 

    
**while loop**
n=5
while n>=0 :
    print(n,end=" ")
    n-=1        output =5 4 3 2 1 0 


'''
def getindex():
    sum=0
    for x in range(10):
        sum=sum+x
        if(sum>=20):
            return x
            break

print(getindex())







