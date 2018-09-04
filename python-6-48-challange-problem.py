# spy game
def spygame(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(spygame([0,0,7,8,2,5]))

# prime numbers
def count_primes(num):
    # check for 0 or 1
    if num < 2:
        return 0
    # 2 or greater
    
    # store your prime numbers
    primes = [2]
    # counter
    x = 3
    while x <= num:
        # check if x prime
        for y in range(3,x,2):
            if x%y ==0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
