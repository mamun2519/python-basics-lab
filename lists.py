
# syntax the list
myList = [1, 2, 3, 4, 5 , 6]

# accessing the list
print(myList[0])  # Output: 1
print(myList[2:6])  # Output: 3
print(myList[:3])  # Output: 6

# change the value
myList[0] = 10
print(myList)  # Output: [10, 2, 3, 4

# add the value
myList.append(7) # add last
print(myList)  # Output: [10, 2, 3, 4, 5, 6, 7]
myList.insert(5, 20) # add first
print(myList)  # Output: [10, 2, 3, 4, 5, 20, 6, 7]


# remove the value
myList.remove(20) # remove the value
print(myList)  # Output: [10, 2, 3, 4, 5, 6, 7]
myList.pop(0) # remove the last value
print(myList)  # Output: [10, 2, 3, 4`, 5, 6]

# loop the list

for i in myList:
    print(i)

for i in range(len(myList)):
    print(myList[i])

# list comprehension
squaredList = [x**2 for x in myList]
print(squaredList)  # Output: [100, 4, 9, 16, 25, 36]

# sort the list
myList.sort( )     
print(myList)  # Output: [2, 3, 4, 5, 6, 10]

# count
print(myList.count(4))  # Output: 1
print(myList.index(4))  # Output: 2