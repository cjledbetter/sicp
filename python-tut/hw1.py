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
