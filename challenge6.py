#Challenge 6: Find the longest word in a sentence

from typing import List

def find_longest_word(sentence: str) -> str:
    sentence_arr: List[str] = sentence.split()
    longest_word: str = ""
    for word in sentence_arr:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence: str = "The quick brown fox jumps over the lazy stegosaurus"

longest_word: str = find_longest_word(sentence)

print(f"Sentence: \"{sentence}\"")
print(f"The longest word is: \"{longest_word}\"")