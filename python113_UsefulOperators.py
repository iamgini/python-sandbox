#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
for num in range(10,100,10):
    print(num)

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

for item,letter in enumerate('abcde'):
    print(item)
    print(letter)
    print('\n')
# zip operator
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = ['a','b','c','c']
for item in zip(mylist1,mylist2,mylist3):    
    print(item)
uniq.mylist3()
# in keyword
if 'a' in "in a world":
    print("a is in the word")

# min and max
mylist1 = [1,2,3]
print(f'Min={min(mylist1)}')
print(f'Max={max(mylist1)}')

# shuffle function
from random import shuffle
mylist1 = [1,2,3,4,5,6,7,8,9]
shuffle(mylist1)
print(mylist1)

# randint
from random import randint
print(randint(0,100))

# input function
result = input('Enter a number:')
print(result)

