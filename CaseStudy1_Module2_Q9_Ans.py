# Write a for loop that prints all elements of a list and their position in the list.
#a = [4,7,3,2,5,9]

a = [4,7,3,2,5,9]
for postion, value in enumerate(a,start=0):
    print 'Value',value,'at position',postion