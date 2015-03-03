# Homework 2
# Due Sunday, Feb 1 at 23:59
# Always write the final code yourself
# Cite any websites you referenced
# Use the PEP-8 checker for full style points:
# https://pypi.python.org/pypi/pep8
import calendar


def string_distance(s1, s2):
    '''Counts the number of positions at which two strings have different
    characters. If the strings are of unequal length, you should count the
    missing characters as disagreements. Do not count uppercase and
    lowercase letters as different.
    '''
    s1 = s1.lower()
    s2 = s2.lower()
    count = 0
    if (len(s1) <= len(s2)):
        for i in range(0, len(s1)):
            if (s1[i] != s2[i]):
                count += 1
        count = count + len(s2) - len(s1)
    else:
        for i in range(0, len(s2)):
            if (s1[i] != s2[i]):
                count += 1
        count = count + len(s1) - len(s2)
    return count



def chars_after(s1, s2):
    '''Return a list of unique characters in s2 such that the index at
    which the character first occurs in s2 is greater than the index
    that the character first occurs in s1. If a character does not
    occur in s1 but occurs in s2 then it should be among those
    returned. The order of chars in the returned list does not matter.
    Different case (Upper/lower) counts as different characters this time
    '''
    uniques = []
    for i in range(0, len(s2)):
        occurs = 0
        index = -1
        for j in range(0, len(s1)):
            if (occurs == 0 and s1[j] == s2[i]):
                occurs = 1
                index = j
        if (index < i or index == -1):
            uniques = uniques + [s2[i]]

    return uniques


def convert_date(s):
    ''' Converts a date string of the form "mm/dd/yyyy" to a string of the
    form "Month date, year". You should be able to handle (any number of)
    leading zeros, but can assume the input will correspond to a valid date.
    The month_name attribute of the calendar module may be useful:
    https://docs.python.org/3.4/library/calendar.html
    '''
    slist = s.split('/')
    month = slist[0][len(slist[0])-2:]
    day = slist[1][len(slist[1])-2:]
    year = slist[2][len(slist[2])-4:]

    months = ["","January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"]

    return months[int(month)] + " " + repr(int(day)) + ", " + year



def my_sort(lst):
    '''Return a sorted copy of a list. Do not modify the original list. Do
    not use Python's built in sorted method or [].sort(). You may use
    any sorting algorithm of your choice.  Running time does not
    matter.
    '''
    sortedList = lst
    for i in range(len(sortedList)):
        for j in range(len(sortedList) - 1, i, -1):
            if (sortedList[j] < sortedList[j-1]):
                temp = sortedList[j]
                sortedList[j] = sortedList[j-1]
                sortedList[j-1] = temp

    return sortedList


def frequency_dict(s):
    ''' First create a dictionary where each key is a character that appears
    in the input string, and the value is a list of the indices at which that
    character appears. Then format this dictionary as seen in the examples,
    and return the resulting string.

    Treat lower and upper case characters the same, and just include the
    lowercase version in your dictionary. Pairs should be listed in
    alphabetical order by key (use your my_sort function for this).
    '''
    s = s.lower()
    freqDict = {}

    for i in range(len(s)):
        if s[i] in freqDict:
            freqDict[s[i]] = freqDict[s[i]] + [i]
        else:
            freqDict[s[i]] = [i]
    
    keys = []
    for k, v in freqDict.items():
        keys.append(k)

    keys = my_sort(keys)

    outputString = keys[0] + "=" + repr(freqDict[keys[0]])

    for i in range(1, len(keys)):
        outputString = outputString + ", " + keys[i] + "=" + repr(freqDict[keys[i]])

    return outputString

def my_permute(lst):
    ''' Returns a list of all permutations of a list. Do not use any of
    Python's builtin functions from the itertools library. Sort the list
    using my_sort before returning it, and remove any duplicates as well.
    Note that the set() trick won't work right off the bat -- why not?
    '''
    outList = [[lst[0]]]
    
    for i in range(1, len(lst)):
        next = lst[i]
        newAdds = []
        for j in outList:
            for k in range(len(j) + 1):
                newAdds += [j[:k] + [next] + j[k:]]
        outList = newAdds

    final = []
    for i in range(len(outList)):
        if outList[i] not in outList[i+1:]:
            final.append(outList[i])
    return my_sort(final)

def main():
    pass

if __name__ == "__main__":
    main()
