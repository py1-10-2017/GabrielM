# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

# for number in range(1, 1001, 2):
#     print number

# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.

# for number in range(5, 1000001, 5):
#     print number

# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

a = [1, 2, 5, 10, 255, 3]
sum = 0

for number in a:
    sum += number
print "The sum is", sum 

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

print "The average of the numbers in the list is", sum / len(a)