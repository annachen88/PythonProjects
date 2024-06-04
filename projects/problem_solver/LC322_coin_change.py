"""
File: LC322_coin_change.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
    """
    # DFS and dynamic programming bottom-up
    # input = [1, 3, 4, 5] ,amount = 7
    # dp[0] = 0
    # dp[1] = 1
    # dp[2] = 2
    # dp[3] = 1
    # dp[4] = 1
    # dp[5] = 1
    # dp[6] = 2
    # dp[7] = 1 + dp[6]

    def coinChange(self, coins: List[int], amount: int) -> int:
        # init max -> amount + 1
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if (a-c) >= 0: #keep searching
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount + 1 else -1
        # if dp[amount] != amount + 1 then return dp[amount] else -1


def main():
    coins = [1, 3, 4, 5]
    amount = 7
    sol = Solution()
    result = sol.coinChange(coins,amount)
    print(result)


if __name__ == "__main__":
    main()
