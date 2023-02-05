"""Write a Python program to triple all numbers 
of a given list of integers. Use Python map."""

num_of_element = int(input("How many elements you want?: "))
lst = []
for i in range(num_of_element):
    element = int(input("Enter element: "))
    lst.append(element)
print("\nList: ", lst)

result = list(map(lambda x: x*3, lst))
print("\nTriple of list numbers: ")
print(result)

