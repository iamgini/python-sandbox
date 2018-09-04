# function to make 1st and 4th letter to uppercase
def old_macdonald(name):
    first_letter = name[0]
    inbtw_letter = name[1:3]
    fourth_letter = name[3]
    rest_letters = name[4:]
    return first_letter.upper() + inbtw_letter + fourth_letter.upper() + rest_letters

print(old_macdonald("macdonald"))
# same thing using capitalize
def new_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()

print(new_macdonald("macdonald"))

#reverse sentence 
def master_yoda(text):
    word_list = text.split()
    r_word_list = word_list[::-1]
    return " ".join(r_word_list) #join with a space instead of printing list

print(master_yoda("I am ready"))

#alost there - to return True if n within 10 of 100 or 200
# 90 - True
# 104 - True
# 150 - False
# 209 - True
def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <=10) #abs will return the absolute value of the number

print(almost_there(105))