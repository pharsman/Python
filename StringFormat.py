animal = 'cow'
item = 'moon'
# print("The {} jumped over the {} ".format(animal, item))
# print("The {1} jumped over the {0} ".format(item, animal)) # positional argument
# print("The {a} jumped over the {b} ".format(a = 'cow', b = 'moon')) # keyword argument



text = "The {} jumped over the {}"
# print(text.format(animal, item))



name = 'Bro'
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}, Nice to meet you".format(name)) 
# print("Hello, my name is {:<10}, Nice to meet you".format(name)) 
# print("Hello, my name is {:>10}, Nice to meet you".format(name))
# print("Hello, my name is {:^10}, Nice to meet you".format(name)) # center



pi = 3.14159
print("The number pi is {:.4f}".format(pi))

number = 1000
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))
