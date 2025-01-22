from stringoperations import count_words, replace_word

def main():
    text = "Python is a great programming language :3"
    
    # Word count
    word_count = count_words(text)
    print(f"Number of words per line: {word_count}")
    
    # Replacing the word
    new_text = replace_word(text, "Python", "JavaScript")
    print(f"Modified text: {new_text}")

if __name__ == "__main__":
    main()
