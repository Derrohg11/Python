name = "Derrick"
animal = "Octopus"

quote = "It is a beautiful day!"
another_quote = 'Octo says "Hello!"'

#print(quote[8:17])
# print(name[::1])

# layout = "*" + "-" * 20 + "*"
# print(layout)

# first_name = "Derrick"
# last_name = "Mwangi"

# print(len(first_name))
# print(first_name.capitalize())
# print(first_name.swapcase())

#--------------Stripping whitespace-----------------
language = "     Python     "
print(language.rstrip())
print(language.lstrip())
print(language.strip())

#-----------------replacing strings-----------------
hello = "Hello, world!"
print(hello.replace("world", "Python"))

print(hello.count("o"))
