"""
File: LC121_buy_and_sell_stock.py
Name: Anna
-------------------------
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

from typing import List


class Solution:
    """
    Hint : Use Two Pointer with buy and sell timing
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
    """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pinter_buy = 0
        right_pointer_sell = 1
        max_profit = 0
        for i in range(len(prices)):
            if prices[left_pinter_buy] < prices[right_pointer_sell]:
                if prices[right_pointer_sell] - prices[left_pinter_buy] > max_profit:
                    max_profit = (prices[right_pointer_sell] - prices[left_pinter_buy])
            else:
                if prices[left_pinter_buy] > prices[i]:
                    left_pinter_buy = i
                if prices[right_pointer_sell] < prices[i]:
                    right_pointer_sell = i
        return max_profit

def main():
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    result = sol.maxProfit(prices)
    print(result)


if __name__ == "__main__":
    main()
