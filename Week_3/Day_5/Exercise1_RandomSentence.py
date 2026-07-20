# 🌟 Exercise 1 — Random Sentence Generator
import random
from pathlib import Path

def get_words_from_file(file_path):
    file_path = Path(__file__).parent / "words.txt"
    with open(file_path, "r") as f:
        content = f.read()
    return content.split()

def get_random_sentence(length):
    words = get_words_from_file("words.text")
    chosen = [random.choice(words) for _ in range(length)]
    return " ".join(chosen)

def main():
    # get input, validate, generate sentence
    try: 
        length = int(input("Enter sentence length (2-20): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    if length < 2 or length > 20:
        print("Length must be between 2 and 20.")
        return
    
    sentence = get_random_sentence(length)
    print(f"Random sentence: {sentence}")   

main()