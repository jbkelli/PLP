# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

#creating an empty list called my-list
my_list = []

#appending to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting at second position
my_list.insert(1, 15)

#extending my_list using another list
my_list.extend([50, 60, 70])

#removing the last element from the list
my_list.pop()

#sorting my_list in ascending order
sorted(my_list)

#finding and printing the index of 30
print(my_list.index(30))