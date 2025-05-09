#Challenge 4: Fizzbuzz

#Prints all numbers from 1-100
#Replaces number with Fizz when number is divisable with 3
#Replaces number with Buzz when number is divisable with 5
#Replaces number with FizzBuzz when number is divisable with 3 and 5

#Flag used to skip the input iteration
skip: bool = False

print("Press enter to generate next number\nType 'skip' to print all numbers\nType 'exit' to exit program")

for i in range(1, 101):

    if skip == False:
        user_input: str = input() #Enters new line when user presses enter
    else:
        print() #New line

    if user_input == "skip":
        skip = True

    if user_input == "exit":
        break

    if i % 15 == 0:
        print("Fizzbuzz ", end="")
    elif i % 3 == 0:
        print("Fizz ", end="")
    elif i % 5 == 0:
        print("Buzz ", end="")
    else:
        print(str(i) + " ", end="")

print("\n\nExiting program...")