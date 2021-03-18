"""
Question: Wiggle Subsequence
Given an integer array nums, return the length of the longest wiggle sequence.
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.
- For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
- In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000

Follow up: Could you solve this in O(n) time?
"""
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        lenN = len(nums)
        i = 1
        while i < lenN and nums[i] == nums[i-1]: i += 1
        if i == lenN:
            return 1
        up = nums[i-1] > nums[i]
        ans = 1
        while i < lenN:
            if (up and nums[i] < nums[i-1]) or (not up and nums[i] > nums[i-1]):
                up = not up
                ans += 1
            i += 1
        return ans