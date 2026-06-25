# empty_tuple = ()
# print(empty_tuple)

# colors = ("Red", "Green", "Blue", "Yellow", "Purple")
# print(colors)

# single_fruit = ("Apple",) # Note the comma at the end to indicate it's a tuple
# print(single_fruit)

# list_to_tuple = tuple([1,2,3])
# print(list_to_tuple)

# string_to_tuple = tuple("Hello")
# print(string_to_tuple)

# x,y,z = (1, 2, 3)
# print(x)
# print(y)
# print(z)

# first, *rest = (1, 2, 3, 4, 5)
# print(first)  # Output: 1
# print(rest)   # Output: [2, 3, 4, 5]

# my_tuple = (1,2,2,3,2,4,5)
# print(my_tuple.count(2))  # Output: 3
# print(my_tuple.index(3))  # Output: 3

# from collections import namedtuple


# person = namedtuple("Person", ["name", "age", "city"])
# Derrick = person ("Derrick", 30, "Nairobi")
# print(Derrick.name)  # Output: Derrick
# print(Derrick.age)   # Output: 30   
# print(Derrick.city)  # Output: Nairobi

# days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# from datetime import datetime
# current_time = datetime.now()
# print(current_time)

from collections import namedtuple

# Point = namedtuple("Point", ["x", "y"])
# p = Point(3, 4)
# print(p.x)  # Output: 3
# print(p.y)  # Output: 4

# Person = namedtuple("Person", ["name", "age", "city"])
# Derrick = Person("Derrick", 30, "Nairobi")
# print(Derrick.name)  
# print(Derrick.age)
# print(Derrick.city)

my_tuple = (3,1,4,1,5,9)

# sorted_tuple = tuple(sorted(my_tuple))
# print(sorted_tuple)

# reversed_sorted = tuple(sorted(my_tuple, reverse = True))
# print(reversed_sorted)

# numbers = (1,2,3,4,5)
# squared_numbers = (n**2 for n in numbers)

# squared_tuple = tuple(squared_numbers)
# print(squared_tuple)


# numbers = (2,4,6,8,10)
# even_numbers = (n for n in numbers if n % 2 == 0)
# even_tuple_power3 = tuple(n**3 for n in even_numbers)

# reversed_tuple = tuple(reversed(even_tuple_power3))
# print(reversed_tuple)

# cubes = tuple(n**3 for n in range(1, 11) if n % 2 == 0)
# reversed_cubes = tuple(sorted(cubes, reverse=True))
# print(reversed_cubes)

# names = ("Alice", "Bob", "Charlie")
# ages = (25, 30, 35)

# for person in zip(names, ages):
#     print(person)

fruits = ("Apple", "Banana", "Cherry")
prices = (40,10,30)

for fruit, price in zip(fruits, prices):
    print(f"The price of {fruit} is {price} shillings.")