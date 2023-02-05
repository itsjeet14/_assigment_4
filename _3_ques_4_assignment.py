"""Write a Python program to square the elements 
of a list using map() function."""

num_of_element = int(input("How many elements you want?: "))
lst = []
for i in range(num_of_element):
    element = int(input("Enter element: "))
    lst.append(element)
print("\nList: ", lst)

result = list(map(lambda x: x**2, lst))
print("\nSquare the elements of the list: ")
print(result)