# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

def is_even(num):
    if (num % 2) == 0:
        return True
    if (num % 2) == 1:
        return False

print(is_even(num))

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even2(num):
    if (num % 2) == 0:
        return "Even!"
    if (num % 2) == 1:
        return "Odd"
print(is_even2(num))