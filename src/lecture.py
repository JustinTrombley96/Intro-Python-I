#String interpolation
name = "Sean"
print(f"Hello {name}") #Hello Sean

# Are variables mutable or immutable?
# Strings are immutable because they cannot be changed, they create a new instance of the string.
# Arrays are mutable because the original changes. Arrays in Python are called Lists.
name = "Will"
name += "ie"
print(f"{name}") #Willie

# Printing an ID
id(name)
print(f"{id(name)}")

# This is true, name and name2 return the same ID.
name ="Benny"
name2 = name
print(id(name))
print(id(name2))
print(id(name) == id(name2)) #True
print((name) == (name2)) #True
print((name is name2)) #True
print(id(name2) is id(name)) #False
#The is keyword is used to test if two variables refer to the same object.
#The test returns True if the two objects are the same object.
#The test returns False if they are not the same object, even if the two objects are 100% equal.

# firstName has already been set. Changing name will only create a new instance of name and not replace the old instance. 
name = "Justin"
firstName = name
name = "Bob"
print(firstName) #Justin

# Create an empty list
p = []

# Create a list with some numbers
q =[1, 2, 3, 4, 5]

p.append(12)

print(p) #[12]
print(q) #[1, 2, 3, 4, 5,]

# Print each individual element in q on a new line. elem is a banana.
for elem in q:
    print(elem)
    #1
    #2
    #3
    #4
    #5

# Loop up throught a list's indices
# Range does not include the last element
# len(q) == 5
for i in range(0, len(q)):
    print(q[i])
    #1
    #2
    #3
    #4
    #5

# Loop through both indices and elements
for (i, x) in enumerate(q):
    print(i, x)
    #0 1
    #1 2
    #2 3
    #3 4
    #4 5

    # dicts (dictionaries) are analogous to JS objects
    # create an empty dict
    d = {}

    # allows you to associate keys with values
    e = {"foo": 12, "bar": 20}
    f = {1: 11, 2: 22}
    print(e["foo"])

    # iterate through our dict
    # k is the key
    for k, v in e.items(): 
        print(k, v) 
        #foo 12
        #bar 20

    for v in e.values(): 
        print(v)
        #12
        #20
evens_1 = [0, 2, 4, 6, 8, 10]
evens_2 = [i for i in range(11) if i % 2 == 0]
print(evens_1) #[0, 2, 4, 6, 8, 10]
print(evens_2) #[0, 2, 4, 6, 8, 10]
print(evens_1 == evens_2) #True

# dict where the keys are int indices with values as even numbers
d = {i: x for i, x in enumerate(evens_1)}
print(d) # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}