# Task: Sum the elements in a list
# Write a recursive function that finds the sum of all elements in a given list of numbers.

def sum_elements(nums):
    if len(nums) == 0:
        return 0

    return nums[0] + sum_elements(nums[1:])


print(sum_elements([1, 2, 3, 4, 5]))  # 15
print(sum_elements([10, -5, 3]))  # 8



# Task: Factorial of a number
# Write a recursive function that calculates the factorial of a given number n.

def fact(n):
    if n == 0 or n == 1:  
        return 1

    return n * fact(n - 1)

print(fact(5))  # 120
print(fact(3))  # 6



# Task: Reverse a number
# Write a recursive function that takes a number and returns the number in reverse.

def reverse_number(n):
    n = str(n)  # Convert number to string

    if len(n) == 1:  # Base case: single-digit number
        return n

    return n[-1] + reverse_number(n[:-1])  # Get last digit + recursive call


print(reverse_number(1234))  # 4321



# Task: Finding the largest number in a list
# Write a recursive function that finds the largest number in a given list of numbers.

def get_biggest(nums):
    if len(nums) == 1:
        return nums[0]

    biggest_in_rest = get_biggest(nums[1:])
    return nums[0] if nums[0] > biggest_in_rest else biggest_in_rest


# Пример:
print(get_biggest([1, 5, 3, 9, 2]))  # 9
print(get_biggest([10, 20, 30]))  # 30
