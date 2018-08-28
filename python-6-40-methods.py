#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
mylist = [x for x in range(1,10)]
print(mylist)
mylist.append(100) #append an item to mylist
print(mylist)
mylist.pop() #remove item from top
print(mylist) 
#type your list variable, then '.' and find those available methods or functions
mylist.insert(5,999)
print(mylist) 