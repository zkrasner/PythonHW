""" Homework 5
-- Due Sunday, Feb. 22th at 23:59
-- Always write the final code yourself
-- Cite any websites you referenced
-- Use the PEP-8 checker for full style points:
https://pypi.python.org/pypi/pep8
"""

class LogFileManager(object):
    '''Write a context manager which ensures that file objects are closed.
    Additionally, log out to a file called file_io_log.txt. The log
    should record the command used to open the file as well as any
    errors.  The format of the log should be
    'open(...) -> Exception: None\n' if there were no errors and
    if an error occurs record the details of the error after 'Exception:'
    'open(...) -> Exception: <class 'io.UnsupportedOperation'>: not writable\n'
    Here's the PEP on with statments https://www.python.org/dev/peps/pep-0343/
    Search for 'The translation of the above' on that page for a good
    explanation of the with statement
    '''
    def __init__(self, filename, iotype):
        self.filename = filename
        self.iotype = iotype

    def __enter__(self):
        self.handle = open(self.filename, self.iotype)
        return self.handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.handle.close()
        with open("file_io_log.txt", "w") as out:
            if exc_type is None:
                s = 'open({!r}, {!r}) -> Exception: None\n'
                s = s.format(self.filename, self.iotype)
                out.write(s)
            else:
                s = 'open({!r}, {!r}) -> Exception: {} {}\n'
                s = s.format(self.filename, self.iotype, exc_type,exc_val)
                out.write(s)
        return True



class Leibniz(object):
    '''Write a custom generator class for the Leibniz infinite series,
    which converges to pi/4.
    See here: http://en.wikipedia.org/wiki/Leibniz_series

    Figure out which magic method(s) you need to implement.
    In addition, write a method list_leibniz(n) that returns a list of
    the first n terms of the series.
    '''
    def __init__(self):
        self.index = 0
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        self.n += ((-1)**self.index)/(2*self.index + 1)
        self.index += 1
        return self.n

    def list_leibniz(self, n):
        self.index = 0
        self.n = 0
        ret = list()
        for i in range(n):
            ret.insert(i, self.next())
        return ret


class InvalidFormatException(Exception):
    ''' For use below. '''
    pass


def csv_to_dict(infile):
    ''' Convert a csv file to a list of dictionaries, and return the list.
    For instance, a file containing:
    student,age,gender
    Anne,22,female
    John,21,male

    should be converted to the list:
    [{'student': 'Anne', 'age': 22, 'gender': 'female'},
     {'student': 'John', 'age': 21, 'gender': 'male'}]

    -- If the csvfile (i.e. the argument "infile") does not exist, catch
       the FileNotFoundError, and raise a new exception with the message
       "No such file"
    -- You may assume that a single comma separates each column.
    -- If the file is properly formatted, the number of columns in each row
       will the be same. If this is not the case,
       raise an InvalidFormatException
    -- You may assume that the first row of the csv file contains field names.

    Do not use the DictReader method of the csv module -- your job is to
    implement this behavior yourself.
    '''
    ret_list = list()
    try:
        f = open(infile)
        l = f.readlines()
        f.close()
    except FileNotFoundError:
        raise Exception("No such file")

    labels = l[0][:-1].split(',')
    for i in range(1, len(l)):
        this_dict = dict()
        if i != len(l) - 1:
            data = l[i][:-1].split(',')
        else:
            data = l[i].split(',')
        if len(data) != len(labels):
            raise InvalidFormatException
        for j in range(len(labels)):
            this_dict[labels[j]] = data[j]
        ret_list.append(this_dict)
    return ret_list


def encode_text(codefile, infile, outfile):
    ''' Encode the text in infile according to the mappings in codefile,
    and write the result to outfile. If either infile or codefile
    does not exist, catch the I/O exception, and raise a new exception
    with the message "No such file".

    The codefile will contain mappings, one per line, of one character
    to another: for instance, a,b means that 'a' should be mapped to 'b'
    in the encoded string. If a character is not mapped in the codefile,
    it should not be changed in the output.
    Look at dir('') for useful functions

    If any line in the input file doesn't match this format, or if one
    character is mapped to multiple other characters, raise an
    InvalidFormatException.
    '''
    try:
        with open(infile) as inf:

            code_map = getMappings(codefile, 0)

            input_lines = inf.readlines()

            code(input_lines, code_map, outfile)

    except IOError:
        raise Exception("No such file")


def decode_text(codefile, infile, outfile):
    '''Decode the text in infile, assuming that it was encoded
    according to the mapping in codefile. Write the result to outfile.
    If either infile or codefile does notexist,
    use the same procedure as before.

    Keep your code DRY (Don't Repeat Yourself). Feel free to write
    auxiliary functions that will be called by both encode_text
    and decode_text.
    '''
    try:
        with open(infile) as inf:

            code_map = getMappings(codefile, 1)

            input_lines = inf.readlines()

            code(input_lines, code_map, outfile)

    except IOError:
        raise Exception("No such file")


def getMappings(codefile, direction):
    with open(codefile) as code:

        mappings = code.read().splitlines()
        code_map = dict()
        for i in range(len(mappings)):
            s = mappings[i].split(",")
            if direction == 0:
                if s[0] not in code_map.keys() or len(s) != 2:
                        code_map[s[0]] = s[1]
                else:
                    raise InvalidFormatException
            else:
                if s[1] not in code_map.keys() or len(s) != 2:
                        code_map[s[1]] = s[0]
                else:
                    raise InvalidFormatException
        return code_map


def code(inputlines, mappings, outfile):
    with open(outfile, 'w') as out:

        for i in range(len(inputlines)):
            for j in range(len(inputlines[i])):
                if inputlines[i][j] in mappings.keys():
                    out.write(mappings[inputlines[i][j]])
                else:
                    out.write(inputlines[i][j])
        out.close()


def main():
    pass


if __name__ == "__main__":
    main()
