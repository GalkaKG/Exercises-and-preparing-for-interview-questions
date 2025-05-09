def reverse_words(sentence):
    # Split the sentence into words, reverse the list, and join them back
    return ' '.join(sentence.split()[::-1])

# Example
print(reverse_words("Hello World"))  # Output: "World Hello"
print(reverse_words("Python is fun"))  # Output: "fun is Python"
print(reverse_words("I love programming"))  # Output: "programming love I"  
print(reverse_words("The quick brown fox"))  # Output: "fox brown quick The"
print(reverse_words("A B C D E F G"))  # Output: "G F E D C B A"