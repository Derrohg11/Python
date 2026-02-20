def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def square(num):
    return num ** 2

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Number: {number}")
print(f"Even or Odd: {check_even(number)}")
print(f"Sign: {check_sign(number)}")
print(f"Square: {square(number)}")
    
