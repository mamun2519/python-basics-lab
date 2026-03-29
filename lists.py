
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