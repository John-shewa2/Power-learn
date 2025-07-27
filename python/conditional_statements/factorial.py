# A program that prints the factorial of an integer

number = int(input("Please input a number: "))
factorial = 1
for i in range (1, number+1):
    factorial *= i
print(f"The factorial of {number} is {factorial}")
        


#fibonacci series with while loop
number = int(input("Please enter a number: "))
sum = []
a, b = 0, 1
count = 0

while count < number:
    sum.append(a)
    a, b = b, a + b
    count += 1
print(sum)
