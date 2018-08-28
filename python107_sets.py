#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
#Tuples are immutable
# sets are unordered collections of unique elements
myset = set()
print("myset : ",myset)
myset.add(1)
print("myset : ",myset)
myset.add(2)
print("myset : ",myset)
myset.add(2)
print("myset : ",myset)
newset = [1,1,1,2,2,3,3]
set(newset)
print("newset : ",newset)