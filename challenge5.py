#Challenge 5: Palindrome checker

word: str = input("Enter a word: ")

#Reversing the word
rev_word: str = word[::-1]

if rev_word == word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")