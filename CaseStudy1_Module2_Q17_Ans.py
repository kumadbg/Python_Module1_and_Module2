# By using list comprehension, please write a program to print the list after removing
# delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]
list1=[12,24,35,70,88,120,155]
result = [x for (i, x) in enumerate(list1) if(i % 5 == 0) if(i % 7 == 0)]
print result