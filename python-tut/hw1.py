# Chris Ledbetter
# CS 61A 2017
# auditing class

#ques. 1
# from operator import add, sub
# def a_plus_abs_b(a,b):
#     """
#     >>> a_plus_abs_b(2, 3)
#     5
#     >>> a_plus_abs_b(2,-3)
#     5
#     """

#     if b < 0:
#         f = sub
#     else:
#         f = add
#     return f(a, b)

#ques. 2
def max_two(x, y, z):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.
    >>> max_two(1, 2, 3)
    13
    >>> max_two(5, 3, 1)
    34
    >>> max_two(10, 2, 8)
    164
    >>> max_two(5, 5, 5)
    50
    """
    return max(x*x+y*y, y*y+z*z, z*z+x*x)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return sum([i*i for i in sorted([a, b, c])[1:3]])

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.
    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return True

def t():
    return 1

def f():
    raise RuntimeError

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    len = 1
    while n >= 1:
        print(n)

        if n == 1:
            return len
        elif n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

        len = len + 1
