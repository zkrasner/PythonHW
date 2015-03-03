""" Homework 1
-- Due Monday, Jan. 25th at 23:59
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""


def fizzbuzz(n):
    """ If n is divisible by 3, return "Fizz"
    If n is divisible by 5, return "Buzz"
    If n is divisible by 3 and 5, return "FizzBuzz"
    Else, do nothing.
    """
    if n % 3 == 0:
        if n % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'

def snapcrackle(n):
    """ If n is an int, return "Snap"
    If n is a float, return "Crackle"
    Else, do nothing.
    """
    if isinstance(n, int):
        return "Snap"
    elif isinstance(n, float):
        return "Crackle"


def is_prime(n):
    """ Return True if n is prime and False otherwise.
    Use this function to help write 'nth_prime' below.
    """
    if n < 2:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else: 
        return True


def nth_prime(n):
    """ Return the nth prime number.
    """
    last = 1
    if n < 1:
        return 1
    while n > 0:
        last = last + 1
        if is_prime(last):
            n = n - 1
    else:
        return last



def gcd_iter(n, m):
    """ An iterative function that calculates the GCD of n and m.
    Note that there is a function from the fractions module,
    fractions.gcd(a, b), that computes this -- do not use this
    function, but replicate its behavior exactly (including for
    negative or 0 inputs). See its documentation here:
    https://docs.python.org/3/library/fractions.html
    """
    while m != 0:
        temp = m
        m = n % m
        n = temp
    return n


def gcd_rec(n, m):
    """ A recursive function that calculates the GCD of n and m.
    """
    if m == 0:
        return n
    else:
        return gcd_rec(m, n % m)


def fib_iter(n):
    """ An iterative function that calculates the nth Fibonacci number.
    By convention we will say that the 1st Fibonacci number is 0
    and the 2nd Fibonacci number is 1.
    0 1 1 2 3 5 8 13 
    """

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        f1 = 0
        f2 = 1
        n = n - 2
        while n > 0:
            temp = f2
            f2 = f2 + f1
            f1 = temp
            n = n - 1
        return f2 


def fib_rec(n):
    """ A recursive function that calculates the nth Fibonacci number.
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: 
        return fib_rec(n - 1) + fib_rec(n - 2)


def main():
    pass


if __name__ == "__main__":
    """ Runs main() if we run this file with 'python hw1.py'. """
    main()
