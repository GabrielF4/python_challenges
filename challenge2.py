#Challenge 2: return a sum of 2 values

#Secure input for number 1
while True:
    user_input: str = input("Enter first number: ")
    if user_input.isdigit():
        num1: int = int(user_input)
        break
    else:
        print("Invalid input")
        continue

#Secure input for number 2
while True:
    user_input: str = input("Enter first number: ")
    if user_input.isdigit():
        num2: int = int(user_input)
        break
    else:
        print("Invalid input")
        continue

sum: int = num1 + num2
print(f"The sum of the two numbers are: {sum}")