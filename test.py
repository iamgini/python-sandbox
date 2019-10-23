def findodd(l,r):
  for i in range(l,r):
      #print(i)
      if i % 2 != 0:
          print("\tits is odd")
      #else:
      #    print("\tits is odd")

result = findodd(1,10)
print(result)