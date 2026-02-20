try:
    number = float(input("Enter a number: "))

    if number.is_integer():
        number = int(number)

        if number % 2 == 0:
            print(f"{number} is an Even integer.")
        else:
            print(f"{number} is an Odd integer.")
    else:
        print("Not an integer.")

except ValueError:
    print("Please enter a valid number.")
