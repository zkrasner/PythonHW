""" Homework 3
-- Due Sunday, Feb. 8th at 23:59
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""
import string
from functools import partial

def sort_by_id(seq):
    ''' Sort a list of dictionaries by the key 'id'.
    If this key is not present, its value should be assumed to be 0.
    Return the sorted list. Do not modify the input list
    For full style points, do this in one line of code
    '''
    return list(sorted(seq, key = lambda x : 0 if 'id' not in x else x['id']))


def sort_dict(d):
    ''' Sort a dictionary by value. The function should return
    (not print) a comma separated sorted string of key, value pairs,
    in the form "key=value".
    For full style points, do this in two lines of code or fewer.
    '''
    d = sorted(d.items(), key = lambda x : x[1])
    return ', '.join(['{}={}'.format(k, v) for k,v in d])


def count_char_dict():
    '''Return a dictionary where keys are characters of the alphabet, and
    values are functions that take a string as input and count the
    number of times the character appears in the string.
    Treat uppercase and lowercase letters as different letters.
    For full style points, do not use a for loop.
    The string module might be useful.
    You might run into a gotcha about closures here
    '''
    keys = list(string.ascii_lowercase + string.ascii_uppercase)
    l = list()
    for k in keys:
        l.append(lambda str : str.count(k))
    return dict(zip(keys, l))

def collatz(n, cache={}):
    ''' Use memoization to determine the Collatz sequence starting at integer n.
    See here: http://en.wikipedia.org/wiki/Collatz_conjecture
    Your function should return a tuple. The first element in the tuple
    should be the sequence. If the cache was accessed during computation,
    the second element in the tuple should be the integer key that was used.
    If the cache was not accessed, the second element should default to 0.
    '''
    if n in cache:
        print('using cache on {}'.format(n))
        return (cache[n], n)
    if n == 1:
        cache[1] = [1]
        return(cache[1], 0)
    elif n % 2 == 0:
        t = collatz(n//2)
        cache[n] = [n] + t[0]
        return (cache[n], t[1])
    else :
        t = collatz(3*n+1)
        cache[n] = [n] + t[0]
        return (cache[n], t[1])
    


def my_reduce(f, seq, init):
    '''Implement a function with the same behavior as Python's reduce
    except that you may assume that the second argument is a list as
    opposed to the more general iterable. Also init is required
    See here: https://docs.python.org/3.4/library/functools.html
    Assume f is a valid two argument function
    '''
    if init is None:
        value = seq.pop()
    else:
        value = init
    for element in seq:
        value = f(value, element)
    return value


def my_partial(f, *args, **kwargs):
    '''Implement partial application. Suppose the input f takes p
    positional args and k keyword args. Also p' positional and
    k' keyword arguments are partially applied. Return a function g that takes
    p-p' pos args and k-k' kwargs, and then applies f to the complete
    set of p+k args. If a keyword arg is given to my_partial and then
    again to the resulting function, the behavior is undefined
    '''
    partF = partial(f, *args, **kwargs)
    return lambda *gargs, **gkwargs : partF(*gargs, **gkwargs)


def main():
    pass


if __name__ == "__main__":
    main()
