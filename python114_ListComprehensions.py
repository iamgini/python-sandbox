#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
mylist = [x for x in range(1,10)]
print(mylist)

mylist = [letter for letter in "hellow world"]
print(mylist)

mylist = [x**2 for x in range(1,10)]
print(mylist)

mylist = [x**2 for x in range(1,11) if x%2 == 0]
print(mylist)

mylist = []
for i in [2,4,6]:
    for j in [10,100,1000]:
        mylist.append(i*j)
print(mylist)

