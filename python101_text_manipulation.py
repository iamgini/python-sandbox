#import os
#clear screen
#os.system('clear')  # on linux / os x
#print("\n")
print("#simple print output")
print("hello world. I'm Python. This is \"Awesome\"")
print("\n#with new line and tab")
print("\"First Line\"\nSecond Line\n\tThird Line with Tab") 
print("\n#string operations")
prefix = 'Python'
print("Add 2 strings : " + prefix + " Program")
print("Repeat string : " + prefix * 5)
print("\n2nd character in a word :",prefix[1])
print("\nlast character in a word :",prefix[-1])
print("\nText from a position :", prefix[2:])
print("\nText until a position :", prefix[:3])
print("\nText From-To a position :", prefix[3:5])
print("\nText Remove last char :", prefix[:-2])
print("\nText all but step size diff :", prefix[::2])
print("\nText all but step size diff recerse:", prefix[::-1])

print("\nText to upper :", prefix.upper())
print("\nText to lower :", prefix.lower())
print("\nText split :", prefix.split('h'))

print("\n#label and variable")
a = 10
print("a is",a)
total = a * 10
print("a * 10 =",total, "and a * 2 =", a * 2)
print("Length of a String - len :", len(prefix))
