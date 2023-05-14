import random
var = 2

print(type(var))

var2 = "str"

print(type(var))
#print will tell us it is a string

print(dir(var))

#output with _ are hidden ignore

print(var2.capitalize())
#this will return catpial S in Str


var3 = "9"
print(var3.zfill(3))


number = random.randint(0,100)

print(number)





import random  # import the random module for generating random numbers

var = 2  # assign the value 2 to the variable var

print(type(var))  # print the type of var (should be int)

var2 = "str"  # assign the string "str" to the variable var2

print(type(var))  # print the type of var (should still be int)

print(dir(var))  # print the attributes and methods of var

print(var2.capitalize())  # capitalize the first letter of var2 and print the result

var3 = "9"  # assign the string "9" to the variable var3

print(var3.zfill(3))  # fill the string with leading zeros so that it has a total length of 3 and print the result

number = random.randint(0,100)  # generate a random integer between 0 and 100 and assign it to the variable number

print(number)  # print the value of number (should be a random integer between 0 and 100)
