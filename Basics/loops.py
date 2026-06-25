# for item in iterable:
#     block of code to execute

# for number in range(11):
#     print(number)

# for char in "Hello World":
#     print(char)

# count = 10

# while count> 5:
#     print(count)
#     count -= 1

# while True:
#     user_input = input("Write something (q to quit): ")
#     if user_input == "q":
#         break
#     print(f"You typed: {user_input}")

# for number in range(1,5):
#     if number == 2:
#         print ("Skipping number 2")
#         continue
#     print(number)
# else:
#     print("Loop is done")

# for index, char in enumerate("Hello World"):
#     if (index == 5):
#         continue
#     print(f"Index: {index}, Character: {char}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

# for number in numbers:
#     if number % 2 == 1:
#         continue
#     print(number)

for i in range(1,6):
    for j in range(1,6):
        print(i*j, end="\t")
    print()