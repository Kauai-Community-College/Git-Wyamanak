#---------------------------------------------------------
# Name: Winston Yamanaka
# File Creation Date: 2025-05-08
# Last Edit Date: 2025-05-08
# Description: Messing around with Python variables and stuff
#---------------------------------------------------------

# my starting variables
a = 10000
b = 3
c = 0  # gonna try dividing by zero later... maybe?

# doing some math with the variables
print("Addition:", a + b)        # adding a and b
print("Subtraction:", a - b)     # subtracting b from a
print("Multiplication:", a * b)  # a times b

# dividing a by b, should work fine
print("Division:", a / b)

# trying to divide by zero will crash the program
# print(a / c)  # whoops this breaks the code!
# dividing by zero gives you an error (ZeroDivisionError I think?)

# playing with strings now
greeting = "hello"
target = "world"

# using + to stick them together with a space and an exclamation mark
print(greeting + " " + target + "!")  # should print hello world!

# you can’t subtract strings or anything like that
# print(greeting - target)  # this doesn’t work, gives error

# trying to turn an int into a float and see what type it is
print("Type of b before:", type(b))  # should say int
b = float(b)
print("Type of b after:", type(b))   # now it says float

# trying this with strings doesn’t work unless it’s a number string
# like float("hello") just gives an error, not a number thats why
