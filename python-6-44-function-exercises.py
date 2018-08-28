#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
result = lesser_of_two_evens(40,65)
print(result)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    wordlist = text.split() #split the text to words
    return wordlist[0][0] == wordlist[1][0] #compare first letter of first word with first letter of 2nd word and return true or false
result = animal_crackers('line lain')
print(result)


# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    if a == 20 or b == 20 or (a+b)== 20:
        return True
    else:
        return False

result = makes_twenty(19,1)
print(result)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name): 
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()

result = old_macdonald('macdonald')
print(result)

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(name): 
    return ' '.join(name.split()[::-1])

result = master_yoda('I am home')
print(result)


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    

