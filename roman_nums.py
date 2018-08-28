"""
Roman numeral reading
"""

import re
import str

class RomanError(Exception): pass
class OutOfRangeError(RomanError): pass
class NotIntegerError(RomanError): pass
class InvalidRomanNumeralError(RomanError): pass

def check_valid(s):
    pattern = """
    ^                   #Beginning of string
    M{0,3}              #Thousands, between 0 and 3000
    (CM|CD|D?C{0,3})    #Hundreds place
    (XC|XL|L?X{0,3})    #Tens place
    (IV|VI{0,3})        #Ones place
    $                   #End of string
    """
    return re.search(pattern,s,re.VERBOSE)

romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))


def toRoman(i):
    """
    1. Return Roman numeral rep. for integer i, from 1 to 3999
    2. Fail if given i not in the range of 1 to 3999
    3. Fail if given a non-integer number
    4. Always return roman numeral with uppercase letters
    5. toRoman(fromRoman(s)) == s
    """
    if i < 0 or i > 3999:
        raise OutOfRangeError, "Number must be between 0 and 4000"
    if int(i) <> i:
        raise NotIntegerError, "Number is not an integer"
    answer = ''

    for numeral,integer in romanNumeralMap:
        while i >= integer:
            answer += numeral
            i -= integer

    return answer
    




def fromRoman(s):
    """
    1. Take a valid Roman numeral string s and convert it to an integer
    2. Fail if given an invalid roman numeral
    3. Only accept uppercase letters
    4. fromRoman(toRoman(n)) == n
    """
    if not check_valid(s):
        raise InvalidRomanNumeralError, "This is not a valid Roman Numeral"

    index = 0
    result = 0
    for numeral,integer in romanNumeralMap:

        while s[index:index + len(numeral)] == numeral:
            result += integer
            index += len(numeral)

    return result

if __name__ == '__main__':
    print check_valid('MCMXL')

