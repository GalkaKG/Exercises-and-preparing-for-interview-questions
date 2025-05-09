from collections import Counter

# def most_common_char(s):
#     count = Counter(s)
#     return count.most_common()[0][0]  

def most_common_char(string):
    dict = {}
    s = list(string.replace(' ', ''))

    for char in list(s):
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    # return max(dict, key=dict.get)

    max_count = 0
    max_char = ''
    for key, value in dict.items():
        if max_count < value:
            max_count = value
            max_char = key
    
    return max_char
    

# Example usage
print(most_common_char("aabbccc"))  # 'c'
print(most_common_char("hello world"))  # 'l'
print(most_common_char("python programming"))  # 'p'