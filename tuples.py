
## syntax the tuple
myTuple = (1, 2, 3, 4, 5 , 6)

# accessing the tuple
print(myTuple[0])  # Output: 1
print(len(myTuple))  # Output: 6

# loop the tuple
for i in myTuple:
    print(i)
for i in range(len(myTuple)):
    print(myTuple[i])

# tuple comprehension
squaredTuple = tuple(x**2 for x in myTuple)

# count
print(myTuple.count(4))  # Output: 1