#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
mylist = ["one","two","three"]
print("List : ", mylist)
print("Print from item 2 in List : ", mylist[1:])
newlist = [20,100,30.17]
mylist = mylist + newlist
print("\nNew list : ",mylist)
mylist[0] = "BIG ONE"
print("\nNew list : ",mylist)
mylist.append("Six")
print("\nNew Item in list : ",mylist)
mylist.pop()
print("\nRemoved Item from list : ",mylist)
print("\nShow and Remove Item from list : ",mylist.pop())
newlist.sort()
print("\nSorted list : ",newlist)

# servername: amsd2a-n-b02513,vws.hosttype: VWS,vws.kstemplate: ks.vws.template,vws.memory: 36,vws.operatingstatus: decommisioned
a =  [1, 2, 3, 4, 1, 4, 1].count(1)
print(a)

