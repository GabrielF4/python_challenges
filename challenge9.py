#Challenge 9: Prime generator

from typing import List

#Generate an array with primes based on the sieve of eristosthenes algorithm
def sieve_of_eristosthenes(number: int) -> List[bool]:
    
    arr: List[bool] = []
    
    for i in range(number):
        arr.append(True)

    i = 2    
    while(i * i < number):
        if arr[i]:
            j = i
            while(i * j < number):
                arr[i * j] = False
                j+=1
        i += 1

    return arr

#Prints all primes in the sieve of eristosthenes array
def print_all_primes(arr: List[bool]):
    for i in range(2, len(arr)):
        if arr[i]:
            print("Prime: ", i)

if __name__ == "__main__":

    print("PRIME NUMBER GENERATOR")

    arr: List[bool] = sieve_of_eristosthenes(1_000_000)

    for i in range(2, len(arr)):
        if arr[i]:
            if input("Press enter (write 'exit' to exit program): ") == 'exit':
                exit()
            
            print(i)

#Extra code used while creating program
"""
#Check if a number is prime
def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#Print the last prime of the sieve of eristosthenes array
def print_last_prime(arr):
    i = len(arr) - 1
    while(i > 0):
        if arr[i]:
            print(i)
            break
        i -= 1

#Code to check if a user input is a prime
while(True):
    user_input = input("Enter a number: ")
    if user_input.isdigit():
        break
    else:
        print("Incorrect input. Try again")
number = int(user_input)
print(f"{number} is {"" if prime_check(number) else "not "}prime")

#Code to check if a list of whole numbers are primes or not
test_cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 67, 81, 90]
for i in test_cases:
    print(f"{i} is {"" if prime_check(i) else "not "}prime")

#An algorithm to print primes (Not optimized)
for i in range(2, 1000):
    if prime_check(i):
        if input("Press enter to get next prime (write 'exit' to exit) ") == 'exit':
            exit()
        print(i)
print("Limit reached")

"""