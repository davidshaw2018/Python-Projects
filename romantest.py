"""
Unittests for roman numeral conversion
"""

import roman_nums
import unittest

class KnownValues(unittest.TestCase):

    knownValues = ( (1, 'I'),
                    (2, 'II'),
                    (3, 'III'),
                    (4, 'IV'),
                    (5, 'V'),
                    (6, 'VI'),
                    (7, 'VII'),
                    (8, 'VIII'),
                    (9, 'IX'),
                    (10, 'X'),
                    (50, 'L'),
                    (100, 'C'),
                    (500, 'D'),
                    (1000, 'M'),
                    (31, 'XXXI'),
                    (148, 'CXLVIII'),
                    (294, 'CCXCIV'),
                    (312, 'CCCXII'),
                    (421, 'CDXXI'),
                    (528, 'DXXVIII'),
                    (621, 'DCXXI'),
                    (782, 'DCCLXXXII'),
                    (870, 'DCCCLXX'),
                    (941, 'CMXLI'),
                    (1043, 'MXLIII'),
                    (1110, 'MCX'),
                    (1226, 'MCCXXVI'),
                    (1301, 'MCCCI'),
                    (1485, 'MCDLXXXV'),
                    (1509, 'MDIX'),
                    (1607, 'MDCVII'),
                    (1754, 'MDCCLIV'),
                    (1832, 'MDCCCXXXII'),
                    (1993, 'MCMXCIII'),
                    (2074, 'MMLXXIV'),
                    (2152, 'MMCLII'),
                    (2212, 'MMCCXII'),
                    (2343, 'MMCCCXLIII'),
                    (2499, 'MMCDXCIX'),
                    (2574, 'MMDLXXIV'),
                    (2646, 'MMDCXLVI'),
                    (2723, 'MMDCCXXIII'),
                    (2892, 'MMDCCCXCII'),
                    (2975, 'MMCMLXXV'),
                    (3051, 'MMMLI'),
                    (3185, 'MMMCLXXXV'),
                    (3250, 'MMMCCL'),
                    (3313, 'MMMCCCXIII'),
                    (3408, 'MMMCDVIII'),
                    (3501, 'MMMDI'),
                    (3610, 'MMMDCX'),
                    (3743, 'MMMDCCXLIII'),
                    (3844, 'MMMDCCCXLIV'),
                    (3888, 'MMMDCCCLXXXVIII'),
                    (3940, 'MMMCMXL'),
                    (3999, 'MMMCMXCIX'))                 

    def testToRomanKnownVals(self):
        """
        Test the KnownValues indices
        """

        for integer,numeral in self.knownValues:
            result = roman_nums.toRoman(integer)
            self.assertEqual(numeral,result)

    def testFromRomanKnownVals(self):

        for integer,numeral in self.knownValues:
            result = roman_nums.fromRoman(numeral)
            self.assertEqual(integer,result)

class ToRomanExceptions(unittest.TestCase):

    def testTooLarge(self):
        self.assertRaises(roman_nums.OutOfRangeError,roman_nums.toRoman,4000)

    def testZero(self):
        self.assertRaises(roman_nums.OutOfRangeError,roman_nums.toRoman,0)

    def testNegative(self):
        self.assertRaises(roman_nums.OutOfRangeError,roman_nums.toRoman,-50)

    def testNonInteger(self):
        self.assertRaises(roman_nums.NotIntegerError,roman_nums.toRoman,50.6)

class FromRomanExceptions(unittest.TestCase):

    def testInvalidNumeral(self):
        invalidNums = ('MMMM','CMCM','LL','DD','SV','LC','IIXC')
        for s in invalidNums:
            self.assertRaises(roman_nums.InvalidRomanNumeralError,roman_nums.fromRoman,s)

class SanityCheck(unittest.TestCase):
    

    def testSanity(self):
        "Check that fromRoman(toRoman(n)) == n"
        for integer in range (1,4000):
            numeral = roman_nums.toRoman(integer)
            result = roman_nums.fromRoman(numeral)
            self.assertEqual(integer,result)

    
if __name__ == '__main__':
    unittest.main()