#Challenge 12: Randomize lines in a text

import random as rand
from typing import List

#Modifide print function with title and then the text
def print_text(title: str, text: List[str]):
    
    print(f"\n{title}\n")
    
    for line in text:
        print(line, end=" ")

if __name__ == "__main__":

    #Open file and read text into variable text
    with open("chal12text.txt", encoding="utf-8") as f:
        text: List[str] = f.readlines()

    print_text("Original text:", text)

    #Shuffle the lines in the text
    rand.shuffle(text)

    print_text("\nRandom text:", text)
