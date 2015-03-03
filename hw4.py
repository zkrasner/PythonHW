""" Homework 4
-- Due Sunday, Feb. 15th at 23:59
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""
from functools import total_ordering

def memo(f):
    '''Write a decorator that takes a function f as input and returns a
    memoized version of f. Recall that memoization is the use of a
    cache to store previously computed variables.  When memo(f) is
    called on a previously seen input x, memo(f) should return a tuple
    (f(x), True). When memo(f) is called on a new input y, memo(f)
    should return the tuple (f(y), False). The second element in the
    tuple indicates whether the cache was accessed. Note that f may
    take any number of inputs, but you may assume that these inputs
    are hashable. f will not take any keyword arguments
    '''
    def new_f(*args, cache = {}):
        hashed = hash(tuple(sorted(args)))
        if hashed in cache:
            return (cache[hashed], True)
        else:
            res = f(*args)
            cache[hashed] = res
            return (res, False)
    return new_f

dispatch = {}

def register(token):
    ''' Write a parameterized decorator (a function that
    returns a decorator) that takes a string token as input,
    and returns a decorator that will "register" the decorated
    function under that token in the global dispatch dictionary.
    '''
    
    def new_f(f):
        def inner_f(*args, **kwargs):
            dispatch[token] = f
            return f(*args, **kwargs)
        dispatch[token] = inner_f
        return inner_f
    return new_f



def gcd(a, b):
    ''' A gcd function for use below.'''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

@total_ordering
class Rational(object):
    ''' Implement a rational numbers class. Include the following
    magic methods: init, repr, add, sub, mul, truediv, and
    lt, gt, ge, le, ne, eq.

    Some notes:
    -- Numeric operations should return a new Rational Object
    -- All numbers should be in lowest terms at all times.
    -- Denominators should never be negative (e.g. 2/-3 should be
       written as (-2/3))
    -- If the denominator is 1, only print the numerator.
    -- use functools.total_ordering to supply the comparison methods
       https://docs.python.org/3.4/library/functools.html
    '''

    def __init__(self, numer, denom):
        super().__init__()
        self.numer = numer//gcd(numer, denom)
        self.denom = denom//gcd(numer, denom)
        if self.denom < 0:
            self.denom *= -1
            self.numer *= -1

    def __repr__(self):
        if (self.denom == 1) :
            return '{}'.format(self.numer)
        else :
            return '{}/{}'.format(self.numer, self.denom)
        pass

    def __add__(self, x):
        return Rational(self.numer * x.denom + self.denom * x.numer,
                        self.denom * x.denom)

    def __sub__(self, x):
        return Rational(self.numer * x.denom - self.denom * x.numer,
                        self.denom * x.denom)

    def __mul__(self, x):
        return Rational(self.numer * x.numer, self.denom * x.denom)

    def __truediv__(self, x):
        return Rational(self.numer * x.denom, self.denom * x.numer)
        
    def __lt__(self, x):
        return ((self.numer / self.denom) < (x.numer / x.denom))

    def __eq__(self, x):
        return (self.numer == x.numer and self.denom == x.denom)

class Node(object):
    ''' Implement a node class for a binary search tree.
        See here: http://en.wikipedia.org/wiki/Binary_search_tree
        The examples in the test file illustrate the desired behavior.
        Each method you need to implement has its own docstring
        with further instruction.
        '''

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        '''If the node has neither a left nor right child,
        simply return Node(val). Else, return Node(x, val, y),
        where x and y are recursive calls that return the
        left and right children, respectively.
        '''
        if (self.left == None and self.right == None):
            return 'Node({})'.format(self.val)
        elif (self.left == None):
            return 'Node(None, {},'.format(self.val)+' {})'.format(repr(self.right))
        elif (self.right == None):
            return 'Node(' + repr(self.right) + ', {}, None)'.format(self.val)
        else:
            return 'Node({}, {}, {})'.format(repr(self.left), self.val, repr(self.right))

    def insert(self, element):
        ''' Insert an element into a binary search tree rooted
        at this Node. After insertion, return the modified node.

        Our implementation will allow duplicate nodes. The left subtree
        should contain all elements <= to the current element, and the
        right subtree will contain all elements > the current element.
        '''
        if element <= self.val:
            if self.left == None:
                self.left = Node(element)
            else:
                self.left.insert(element)
        else :
            if self.right == None:
                self.right = Node(element)
            else:
                self.right.insert(element)


    def elements(self):
        ''' Return a list of the elements visited in an inorder traversal:
        http://en.wikipedia.org/wiki/Tree_traversal
        Note that this should be the sorted order if you've inserted all
        elements using your previously defined insert function.
        '''
        l = list()
        if self.left != None:
            l.extend(self.left.elements())
        l.append(self.val)
        if self.right != None:
            l.extend(self.right.elements())
        return l


def main():
    pass

if __name__ == "__main__":
    main()
