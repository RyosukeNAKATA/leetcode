class Solution:
    def intToRoman(self, num: int) -> str:
        """
        :type int
        :rtype: str
        """
        # I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000

        thou = num // M
        mod_1000 = num % M
        five_hund = mod_1000 // D
        mod_500 = mod_1000 % D
        
        hund = mod_500 // C
        mod_100 = mod_500 % C
        fifty = mod_100 // L
        mod_50 = mod_100 % L

        ten = mod_50 // X
        mod_10 = mod_50 % X
        five = mod_10 // V
        mod_5 = mod_10 % V

        one = mod_5

        if hund == 4 or hund == 9:
            

        roman_num = 'M' * thou +\
              'D' * five_hund +\
              'C' * hund +\
              'L' * fifty +\
              'X' * ten +\
              'V' * five +\
              'I' * one
        return roman_num