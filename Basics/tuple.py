dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#Tuple is immutable(Cannot be changed), so the following line will cause an error
#dimensions[0] = 250
#Although you can’t modify a tuple, you can assign a new value to a variable
#that holds a tuple. So if we wanted to change our dimensions, we could
#redefine the entire tuple:
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)