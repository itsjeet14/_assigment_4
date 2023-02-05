"""Write a Python program to create a lambda 
function that adds 25 to a given number passed 
in as an argument."""

num = int(input("Enter a number: "))
result = lambda z: z+ 25
print("\nAddition of %d and 25: "%num, result(num))

