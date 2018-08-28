def myfunc(a,b):
    #return 5% of a+b
    return sum((a,b)) * 0.05

result = myfunc(40,60)
print(result)
# in this case we have arguments limited to 2 and will pop up error when try more than 2 arguments

# so we use *args
def myfunc2(*args):
    # we will take args as this wll be tuple. the name args can be anything like spam or var.
    print(args)
    return sum(args) * 0.05

result = myfunc2(40,60,200,400)
print(result)

def myfunc3(**kwargs): #keyword args
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
    return True

result = myfunc3(fruit='apple', vege='spinach')
print(result)

#You can put it together both as below. 
def myfunc4(*args,**kwargs): 
    print(args)
    print(kwargs) 
    return True
result = myfunc4(1,4,22,fruit='apple', vege='spinach')
print(result)