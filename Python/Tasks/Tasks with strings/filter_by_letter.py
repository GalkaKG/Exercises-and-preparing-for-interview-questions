def filter_by_letter(lst, letter):
    # Return words that start with the given letter (case-insensitive)
    return ', '.join([word for word in lst if word.lower().startswith(letter.lower())])

# Example
print(filter_by_letter(["Apple", "Banana", "Avocado"], "a"))  # Output: ['Apple', 'Avocado']
print(filter_by_letter(["Apple", "Banana", "Avocado"], "b"))  # Output: ['Banana']      
