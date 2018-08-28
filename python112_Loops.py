#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
import socket
import subprocess

a= subprocess.Popen()
mytable = [1,2,3,4,5,6,7,8,9]
mysum = 0
for i in mytable:
    print(i)
    mysum = mysum + i
    if i % 2 == 0:
        print("\tits is even")
    else:
        print("\tits is odd")
print("Sum : %s" %(mysum))    

for letter in "Hellow World":
    print(letter)
letter.replace()
#tup example
mylist = [(1,2),(3,4),(5,6)]
for (a,b) in mylist:
    print(a)
    print(b)
print("\n\n")
for i in mylist:
    for j in i:
        print(j)
d = {'k1':100,'k2':200,'k3':300}
for value in d.values():
    print(value)
print("\n\n")
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1 #or x += 1
else:
    print('x is not less than 5')
print("\n\n")
# use of break, continure, pass
for letter in "hello world":
    if letter == 'o':
        continue
    elif letter == 'r':
        break
    print(letter)




        


    



import urllib.request
urllib.request.urlretrieve()