age = 14

# if age>=18:
#     print("You are an adult.")
# elif age>=13:
#     print("You are a teenager.")
# else:
#     print("You are a minor.")

# age = 20

# has_license = False

# if age>=18:
#     if has_license == True:
#         print("You can drive.")
#     else:
#         print("You need a license to drive.")
# else:
#     print("You are too young to drive.")

#----------------Ternary Operator----------------
# age = 20

# print("adult" if age>=18 else "minor")


# name = "ALICE"
# if name.isupper() and len(name) == 5:
#     print("uppercase and 5 characters")
# else:
#     print("It is not uppercase or not 5 characters")

name = "Gunnar"

match name:
    case "Alice":
        print("Hello, Alice!")
    case "Bob":
        print("Hello, Bob!")
    case "Gunnar":
        print("Hello, Gunnar!")
    case _:
        print("Hello, stranger!")