from dis import dis

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first for-loop goes through a list
for num in the_count:
    print(f"This is count {num}")

# same
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# now going through a mixed list - i is a different data type each time round
for i in change:
    print(f"I have {i}")

# this time we'll build a list
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # lists can do the append method
    elements.append(i)

# after building the list we can print the list items - i becomes the list item
for i in elements:
    print(f"Element was: {i}")
    
dis('''
for num in county:
    print(num)
''')
