""" Homework 6
-- Due Sunday, Mar. 1st at 23:59
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""
import re
import itertools
import os


def phone_numbers(number_file, n):
    ''' Open a file and return the first n phone numbers in the text.
    If there are less then n phone numbers in the file, return as many
    as you can.
    If the file does not exist, raise an Exception with the message
    "No such file"

    A phone number has a 3-digit zip code, 3-digit prefix, 4-digit trunk,
    and optional multi-digit extension. The separators may be spaces,
    dashes, or periods, but should be consistent. The zip code may be
    enclosed in parenthesis. There is one exception to the separator
    consistency rule: the separator between the trunk and the extension
    may be the character "x", to indicate "extension". For instance,
    all of the following are valid: 800-555-1212, (800) 555 1212,
    800.555.1212.1234, (800)-555-1212x1234.
    '''
    try:
        with open(number_file) as nums:
            ret = []
            text = nums.read()
            while n > 0:
                regex = r'\(*\d{3}\)*([^\w\d])\d{3}\1\d{4}(((\1|x)\d+)?)'
                m = re.search(regex, text)
                if m is not None:
                    ret += [m.group().strip()]
                    n -= 1
                    text = text[m.span()[1] + 1:]
                else:
                    n = 0
            return ret
    except:
        raise Exception("No such file")


def sorted_dates(date_file):
    '''Find all the dates in the given file and output a list of the dates
       as strings of the form 'mm/dd/yyyy'.

       The list should be sorted in ascending chronological order.

       dates may be in the form: mm/dd/yyyy|mm/dd/yy
       in the latter case yy translates as yy -> 20yy

       If the file does not exist, raise an Exception with the message
       "No such file"
    '''
    try:
        with open(date_file) as dates:
            ret = []
            text = dates.read()
            d = re.search(r'\d\d/\d\d/(\d{4}|\d\d)', text)
            while d is not None:
                if len(d.group()) == 8:
                    ret += [d.group()[3:5] + '/' + d.group()[0:2] +
                            '/20' + d.group()[6:]]
                else:
                    ret += [d.group()[3:5] + '/' + d.group()[0:2] +
                            d.group()[5:]]
                text = text[d.span()[1]:]
                d = re.search(r'\d\d/\d\d/(\d{4}|\d\d)', text)

                ret = sorted(ret)
                ret.reverse()
                sorted_ret = []
                for l in ret:
                    sorted_ret += [l[3:5] + '/' + l[0:2] + '/' + l[6:]]
            return sorted_ret
    except:
        raise Exception("No such file")


class MerriamWebster():
    ''' Write a class based on the accompanying "words.txt" file,
    which contains 235886 English words, one per line.

    An instance of this class should have one attribute, called "words,"
    which should contain a list of all words in "words.txt" of length > 2
    that start with a lowercase letter.

    This class should support the generator protocol, so we should be
    able to iterate over an instance and easily generate words from
    the self.words sequence, one at a time, as per the test file

    You should also implement the following two methods:

    -- substring(x, y, z ...): This method takes an arbitrary number
    of characters as input, computes all possible orderings of these
    characters, and returns a generator over all words in self.words
    that contain (as a substring) one of these orderings.

    For instance, substring('t', 'i', 'e') should generate all words in which
    any of the substrings "tie", "tei", "ite", "iet", "eti", or "eit" appears.

    For full style points, do this without any for loops! You might find it
    helpful to use Python's builtin "any" function:
    https://docs.python.org/3.4/library/functions.html#any

    -- trie(): Create and return a trie data structure to represent
    the contents of self.words. A trie is a special tree structure for
    efficient manipulation of dictionaries (not in the Python sense --
    but you should use a dictionary to implement it!). The basic idea
    is to share the storage of common prefixes.
    See here: http://en.wikipedia.org/wiki/Trie

    Your implementation should use nested dictionaries. Every word should
    end with the symbol "_". As an example, a trie containing the words
    "ball" and "ballet" would be as follows:
    d = {'b': {'a': {'l': {'l': {'_': None,
                                 'e': {'t': {'_': None}}}}}}}

    see the test file for examples
    '''
    WORDS = 'words.txt'

    def __init__(self):
        self.words = []
        with open(self.WORDS) as merriam:
            all_words = merriam.read().splitlines()

            for w in all_words:
                m = re.match('[a-z]', w)
                if m is not None and len(w) > 2:
                    self.words += [w]

    def __iter__(self):
        return self.words.__iter__()

    def substring(self, *args):
        perms = list((''.join(x) for x in itertools.permutations(list(args))))

        ret = []
        for x in self.words:
            for y in perms:
                if y in x and x not in ret:
                    ret += [x]

        return ret.__iter__()

    def trie(self):
        trie = {}

        for w in self.words:
            current_dict = trie
            for x in range(len(w) + 1):
                if x == len(w):
                    current_dict['_'] = None
                    current_dict = trie
                else:
                    if w[x] in current_dict:
                        current_dict = current_dict[w[x]]
                    else:
                        current_dict[w[x]] = {}
                        current_dict = current_dict[w[x]]
        return trie


def sorted_files(directory):
    ''' Walk the specified directory and generate a list of all files found,
    in increasing order of their size in bytes. The filenames should be
    relative to the root directory, e.g. "directory/.../file.txt",
    rather than "file.txt".
    '''
    ret = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            stat = os.stat(dirpath + '/' + f)
            if stat.st_size not in ret:
                ret[stat.st_size] = dirpath + '/' + f
            else:
                ret[stat.st_size] = [ret[stat.st_size], dirpath + '/' + f]
    order = sorted(ret)
    l = []
    for x in order:
        l += [ret[x]]
    return l


def main():
    pass


if __name__ == "__main__":
    main()
