# A program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

set1 = set()
set2 = set()

for i in range(4):
    values = int(input("Please input elements of set 1: "))
    set1.add(values)
print('set1: ', set1)

for i in range(4):
    values2 = int (input("Please input elements of set 2: "))
    set2.add(values2)
print('set2: ', set2)

set3 = set1.intersection(set2)
print('Common elements of set1 & set2: ', set3)