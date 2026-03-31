num1= int(input("Enter number 1:"))
sign = input("Enter the symbol(/,+,-,*):")
num2 = int(input("Enter number 2:"))

if sign == "/":
    print(f"{num1}/{num2} = ", num1/num2)
elif sign == "+":
    print(f"{num1}+{num2} = ", num1+num2)
elif sign == "-":
    print(f"{num1}-{num2} = ", num1-num2)
elif sign == "*":
    print(f"{num1}*{num2} = ", num1*num2)
else:
    print("Invalid symbol")
    