from collections import Counter

def most_common_char(s):
    count = Counter(s)
    return count.most_common()[0][0]  

# Example usage
print(most_common_char("aabbccc"))  # 'c'
print(most_common_char("hello world"))  # 'l'
print(most_common_char("python programming"))  # 'o'