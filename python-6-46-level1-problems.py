# function to make 1st and 4th letter to uppercase
def old_macdonald(name):
    first_letter = name[0]
    inbtw_letter = name[1:3]
    fourth_letter = name[3]
    rest_letters = name[4:]
    return first_letter.upper() + inbtw_letter + fourth_letter.upper() + rest_letters

print (old_macdonald("pythonlearning"))

