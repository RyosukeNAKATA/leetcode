"""
Question: Check If a String Contains All Binary Codes of Size K
Given a binary string s and an integer k.
Return True if every binary code of length k is a substring of s. Otherwise, return False.
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        set_list = set()
        for i in range(len(s)-k+1):
            set_list.add(s[i:i+k])
        if len(set_list) == 2**k:
            return True
        else:
            return False