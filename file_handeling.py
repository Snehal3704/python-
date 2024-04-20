"""
file operation in python 

1.open file
2.read & write(file operation)
3.close the file

f=open('lol.txt','r')

print(f.readline())
or 
for line in f:
    print(line)

or (best)
with open('lol.txt') as f:
    for  line in f:
        print(line)

for reading nad printtinig
with open('lol.txt') as f:
    print(f.read())     // reads everything in the document

**cursor

f.seek(10) // used to curser at 10th position

"""

