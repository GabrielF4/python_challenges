#Challenge 3: Convert minutes to seconds

#Safe input from user
while True:
    user_input: str = input("Enter minutes: ")
    if user_input.isdigit():
        minutes: int = int(user_input)
        break
    print("Invalid input. Only whole numbers are accepted")

seconds: int = minutes * 60

print(f"{minutes} minutes = {seconds} seconds")