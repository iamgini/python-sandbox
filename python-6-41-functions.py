#you can mention def my_function(name = 'NAME'):, in that case NAME will be taken as default without showing an error

def my_function(name):
    '''
    DOCSTRING: This is the information about this function
    INPUT: Your name
    OUTPUT: Hello + Your Name and Return success code
    '''
    print( "hello " + name )
    return "success"

result = my_function("admin")
print(result)
help(my_function)

def dog_chk(mystring):
    if 'dog' in mystring.lower():   #to make sure we search for case-sensitive as well
        return True
    else:
        return False
    # or you can write as -> return 'dog' in mystring.lower()  since it will check, then return if true

result = dog_chk('dog ran away')
print(result)

def pig_latin(word):
    first_letter = word[0]
    if first_letter in 'aeiou': #check if vowel
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

result = pig_latin('oman')
print(result)

