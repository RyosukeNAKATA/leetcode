"""
Question: Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        :type int
        :rtype: str
        """
        thou = num // 1000
        mod_1000 = num % 1000
        hund = mod_1000 // 100
        mod_100 = mod_1000 % 100
        ten = mod_100 // 10
        mod_10 = mod_100 % 10
        one = mod_10
        
        roman_num = ''
        roman_num += 'M' * thou

        if hund is 9:
            roman_num += 'CM'
        elif hund is 8:
            roman_num += 'DCCC'
        elif hund is 7:
            roman_num += 'DCC'
        elif hund is 6:
            roman_num += 'DC'
        elif hund is 5:
            roman_num += 'D'
        elif hund is 4:
            roman_num += 'CD'
        elif hund is 3:
            roman_num += 'CCC'
        elif hund is 2:
            roman_num += 'CC'
        elif hund is 1:
            roman_num += 'C'

        if ten is 9:
            roman_num += 'XC'
        elif ten is 8:
            roman_num += 'LXXX'
        elif ten is 7:
            roman_num += 'LXX'
        elif ten is 6:
            roman_num += 'LX'
        elif ten is 5:
            roman_num += 'L'
        elif ten is 4:
            roman_num += 'XL'
        elif ten is 3:
            roman_num += 'XXX'
        elif ten is 2:
            roman_num += 'XX'
        elif ten is 1:
            roman_num += 'X'

        if one is 9:
            roman_num += 'IX'
        elif one is 8:
            roman_num += 'VIII'
        elif one is 7:
            roman_num += 'VII'
        elif one is 6:
            roman_num += 'VI'
        elif one is 5:
            roman_num += 'V'
        elif one is 4:
            roman_num += 'IV'
        elif one is 3:
            roman_num += 'III'
        elif one is 2:
            roman_num += 'II'
        elif one is 1:
            roman_num += 'I'
        return roman_num