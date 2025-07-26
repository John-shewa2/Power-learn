# A program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

integers = []

for i in range(5):
    values = int(input("Please input five integers:"))
    integers.append(values)
print('List of integers: ',integers)
print('Sum of integers: ', sum(integers))