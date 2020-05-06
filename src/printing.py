"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""



# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
x = 10
y = 2.24552
z = "I like turtles!"

print(f"x is {x}, y is {y}, z is \"{z}\"")


# Use the 'format' string method to print the same thing
list = "x is {x}, y is {y}, z is \"{z}\""
print(list.format(x = 10, y =2.24552, z = "I like turtles!"))




# Finally, print the same thing using an f-string
x = 10
y = 2.24552
z = "I like turtles!"

message = (f"x is {x}, y is {y}, z is \"{z}\"")
print(message)