def add(*args): 
    sum = 0
    args = list(args)
    args[0] = 0
    for i in args: 
        sum += i
    return sum

print(add(1,3,5,7))