#---------------------------------------------------------
# Name: Winston Yamanaka
# File Creation Date: 2025-05-08
# Last Edit Date: 2025-05-08
# Description: Loops
#              just messing with loops lol
#---------------------------------------------------------

# 1. print numbers 1 to 10 with while loop
print("using while loop:")
num = 1  # start from 1
while num <= 10:  # keep going until 10
    print(num)
    num = num + 1  # move to next number

# now same thing but with a for loop
print("now with for loop:")
for n in range(1, 11):  # range goes up to but not including 11
    print(n)

# 2. print numbers from 0 to 50 that are divisible by 3 or 6 or 9
print("divisible by 3, 6, or 9:")
for i in range(0, 51):  # loop from 0 to 50
    if i % 3 == 0 or i % 6 == 0 or i % 9 == 0:
        print(i)

# 3. divide 12 by 2 until the change is small (less than 0.0001)
print("divide by 2 until change < 0.0001")

x = 12  # starting number
change = 1  # just needs to be big at first
steps = 0  # count how many times we do it

while change >= 0.0001:  # keep going until change is small enough
    before = x  # remember last value
    x = x / 2  # divide it by 2
    change = abs(x - before)  # figure out how much it changed
    steps = steps + 1  # add one to the step count

# done!
print("Took", steps, "steps to make the change less than 0.0001")
