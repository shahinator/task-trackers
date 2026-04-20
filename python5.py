"""
Create a generator function even_numbers(n) that yields even

numbers from 0 to n. Raise a custom exception if n is negative.

"""

class negative_number(Exception):
    pass
def even_numbers(n):
    if n < 0:
        raise negative_number("Number cannot be negative")
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

try:
    for num in even_numbers(10):
        print(num)
except negative_number as e:
    print(e)