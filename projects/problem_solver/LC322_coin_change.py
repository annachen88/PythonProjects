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
    # DFS
    def coinChange(self, coins: List[int], amount: int) -> int:


def main():
    n = [3,0,1]
    sol = Solution()
    result = sol.missingNumber(n)
    print(result)
    result = sol.missingNumber2(n)
    print(result)


if __name__ == "__main__":
    main()
