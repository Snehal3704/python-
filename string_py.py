'''
name='snehal'
**Multi line string**
paragraph = """ hsdfsfsijgk
sfjsndkgnskg
sdfnwsngw
woigefn
giodsf
this is a multiline
string"""
print(paragraph)

'''
'''
**string indexing**

in python we can also use negetive indexing for accesing charecters in string
0th index =-(size of array) index

ex:
name='snehal'
print(name[-6]) output = s

so name[-6]= print[0]
    name[-1] = print[5]
so 0th index = -6th index which is also same

$$ in summary for 
^^ 0th idexing: Starts form 0 till size-1
^^ negetive indexing: starts form -size till 1

'''

'''

**slicing in python**

slicing creats new string

the first '['  will be included but the second ']' will be excluded
str = 'abcde'
print(str[1:4])     output: 'bcd'

$$ and for no mentioned case
for [ ,4]   output :'abcd'
this will automatically do *form* 0th index 
for[3, ]    output : 'de'
this will automatically *till* last of the string

ex:
[0,5,2] here 2=steps means skkping 2 elements at a time 
output : 'ace'


'''
'''
**string reverse:**

str = 'snehal'
print(str[::-1])

have to define steps the same direction to the indexning direction

str = 'snehal'
print(str[::-1])
print(str[-1:4:-1])
print(str[-1:0:1])

**lstrip and rstrip function**

lstrip removes all the spaces of the left side a string
tr = '    snehal   '
print(str.lstrip())

rstrip removes all the spaces of the right side of a string
str ='        snehal                '
print(str.rstrip())

''' 
