#!/usr/bin/env python3

"""
Calculate factorial [n!] and Fibonacci series [F(n)] of a number iteratively and recursively
"""


def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively (faster than iterative) """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


print("Num", "\t", "Factorial")
for i in range(11):
    print(i, "\t", fact(i), "\t", factorial(i))


def fibonacci(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fib(n):
    """ Calculates F(n) iteratively (faster than recursion) """
    result = 0
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


print("Num", "\t", "Fibonacci")
for i in range(11):
    print(i, "\t", fib(i), "\t", fibonacci(i))
