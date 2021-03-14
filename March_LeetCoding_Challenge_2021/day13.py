"""
Question: Binary Trees With Factors
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9+7.
"""
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        l = defaultdict(int)
        for a in arr:
            temp = 1
            for b in arr:
                if b > a:
                    break
                temp += (l[b]*l[a/b])
            l[a] = temp
            
        return sum(l.values())%(10**9+7)

# class Solution:
#     def numFactoredBinaryTrees(self, A: List[int]) -> int:
#         A.sort()
#         fmap, ans = defaultdict(), 0
#         for num in A:
#             ways, lim = 1, sqrt(num)
#             for fA in A:
#                 if fA > lim: break
#                 fB = num / fA
#                 if fB in fmap:
#                     ways += fmap[fA] * fmap[fB] * (1 if fA == fB else 2)
#             fmap[num], ans = ways, (ans + ways)
#         return ans % 1000000007