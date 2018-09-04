# find in a list for nearby 3
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:  # or nums[i:i+1] == [3,3]
            return True
    return False

print (has_33([1,3,3]))

#paper doll - repeat each characters 3 times in a string
def paper_doll(text):
    result = ""
    for char in text:
        result += char*3
    return result

print(paper_doll("Hello"))

#blackjack - 
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10 <=21:
        return sum([a,b,c])-10
    else:
        return "BUST"

print(blackjack(5,10,11))



