
programming = "Hello world"

print(programming[2:9]) # Output: Hello world

# sline from the start
print(programming[:5]) # Output: Hello

# modify to upper case
print(programming.upper())
# modify to lower case
print(programming.lower())

# concatination string
first_name = "Mohammad"
last_name = "Mamun"
full_name = first_name + " " + last_name
print(full_name) # Output: Mohammad Mamun

# string count
text = "Hello world, welcome to the world of programming"
count = text.count("w")
print("Count of 'world':", count) # Output: Count of 'world':

# find string
index = text.find("welcome")
print("Index of 'welcome':", index) # Output: Index of 'welcome':

print(text.index("e"))


# indexing string
print(programming[0]) # Output: H
print(programming[6]) # Output: w

# lenth of string
length = len(programming)
print("Length of programming string:", length) # Output: Length of programming string:

# split string
words = programming.split()
print("Words in programming string:", words) # Output: Words in programming string: ['Hello