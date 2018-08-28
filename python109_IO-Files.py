#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
#Tuples are immutable
# 
myfile = open('myfile.txt')
print("print myfile :\n",myfile.read())
myfile.seek(0) #to move read head to start
print("print list of lines from myfile :\n",myfile.readlines())
print("\nAnother method to open")
with open('myfile.txt') as my_newfile:
    content = my_newfile.read()
    print(content)

with open('myfile.txt',mode='r') as f:
    print(f.read())

with open('myfile.txt',mode='a') as f:
    f.write("This is the fourth line added")   

with open('myfile.txt',mode='r') as f:
    print(f.read())
#overwrite if file exist or create if not exist
with open('myfile_new.txt',mode='w') as f:
    f.write("This is new file I have created")   
with open('myfile_new.txt',mode='r') as f:
    print(f.read())   
