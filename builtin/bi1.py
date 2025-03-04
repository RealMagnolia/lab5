import math
import time
import functools


def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)


def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {"Uppercase": upper, "Lowercase": lower}


def is_palindrome(s):
    return s == s[::-1]


def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)


def all_true(t):
    return all(t)

print(multiply_list([1, 2, 3, 4, 5]))  # Output: 120
print(count_case("Hello World!"))  # Output: {'Uppercase': 2, 'Lowercase': 8}
print(is_palindrome("madam"))  # Output: True
print(f"Square root of 25100 after 2123 milliseconds is {delayed_sqrt(25100, 2123)}")
print(all_true((True, True, False)))  # Output: False