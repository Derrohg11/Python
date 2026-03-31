# age = 21

# print(age)

age = 21
time = 9.08
first_name = "Derrick"
is_student = True

# print(type(age))
# print(time)
# print(first_name)
# print(is_student)

# print(isinstance(age, int))

# age = 22
# print(first_name, age, time, is_student)

# time = "Superfast"
# print(first_name, age, time, is_student)

# first_name,last_name = "Derrick", "Mwangi"
# print(first_name, last_name)

# first_name,last_name = last_name, first_name
# print(first_name, last_name)

# DISTANCE = 100
# capitalized variable names are typically used for constants, which are values that should not change throughout the program. By convention, we use uppercase letters to indicate that a variable is intended to be a constant. However, Python does not enforce this, and it is still possible to change the value of a variable that is meant to be a constant
best_time = input("What was your best time?")
print(f"Your best time is {best_time} seconds.")

print(type(best_time))

best_time = float(best_time)
print(type(best_time))
print(f"Your best time is {best_time} seconds.")