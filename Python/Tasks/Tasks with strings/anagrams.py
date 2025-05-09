def are_anagrams(s1, s2):
    """
    Check if two strings are anagrams of each other.        
    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
    """
    if len(s1) != len(s2):
        return False        
    
    # Convert strings to lists of characters      
    list1 = list(s1)
    list2 = list(s2)

    # Sort the lists and compare them 
    list1.sort()
    list2.sort()

    # If they are equal, the strings are anagrams
    return list1 == list2

s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # True