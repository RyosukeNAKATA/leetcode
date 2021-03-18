"""
Question: Best Time to Buy and Sell Stock with Transaction Fee
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buying, selling = 0, -prices[0]
        for i in range(1, len(prices)):
            buying = max(buying, selling + prices[i] - fee)
            selling = max(selling, buying - prices[i])
        return buying