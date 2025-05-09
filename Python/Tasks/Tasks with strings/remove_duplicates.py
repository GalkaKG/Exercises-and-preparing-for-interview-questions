# def remove_duplicates(lst):
#     """
#     Remove duplicates from a list.
#     """
#     return list(set(lst))


def remove_duplicates(lst):
    """
    Remove duplicates from a list while maintaining the order of elements.
    """
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example usage
print(remove_duplicates([1, 2, 2, 3, 1, 2, 4]))  # [1, 2, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 1]))  # [1, 2, 3]
