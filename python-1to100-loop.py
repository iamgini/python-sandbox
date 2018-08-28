# Simple python script to generate numbers from 1 to 100
# But on multiples of three print "Loktar" instead of the number, 
# and on multiples of five print "Ogar". 
# and on multiples of both 3 and 5 your program should print "LoktarOgar".
# author : Gineesh (net.gini@gmail.com)
# run the code as python python-1to100-loop.py

x = 1
while x < 101:
    # check if the value can be divided by both 5 and 3 (multiple of 5 and 3)
    if x % 3 == 0 and x % 5 == 0:
        print('LoktarOgar')
    # check if the value can be divided by 3
    elif x % 3 == 0:
        print('Loktar')
    # check if the value can be divided by 5
    elif x % 5 == 0:
        print('Ogar')
    else:
        print(x)
    x += 1 # x = x + 1 