from stringoperations import count_words, replace_word

def main():
    # Request text from the user
    text = input("Enter text: ")

    # Word count
    word_count = count_words(text)
    print(f"Number of words per line: {word_count}")
    
    # Requesting words to replace
    old_word = input("Enter the word you want to replace: ")
    new_word = input("Enter the word you want to replace it with: ")
    
    # Replacing a word in the text
    new_text = replace_word(text, old_word, new_word)
    print(f"Modified text: {new_text}")

if __name__ == "__main__":
    main()
