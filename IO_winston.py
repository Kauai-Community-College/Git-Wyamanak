#---------------------------------------------------------
# Name: Winston Yamanaka
# File Creation Date: 2025-05-08
# Last Edit Date: 2025-05-08
# Description: Python IO
#              input and output operations
#---------------------------------------------------------

# 1. Ask the user for input and print it back
user_input = input("Say something: ")  # gets input from the user
print("You said:", user_input)         # prints the input back

# 2. Write the input to a file
file = open("output.txt", "w")         # open file for writing (will overwrite if it exists)
file.write(user_input + "\n")          # write the input and add a newline
file.close()                           # always remember to close the file!

# 3. Ask for another input and append it to the same file
another_input = input("Say something else: ")  # new input
file = open("output.txt", "a")                 # open file in append mode
file.write(another_input + "\n")               # add new line to the file
file.close()                                   # close again

print("Both messages saved to output.txt!")    # confirmation message
