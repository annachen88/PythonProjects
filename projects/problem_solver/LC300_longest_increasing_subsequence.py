"""
File: LC300_longest_increasing_subsequence.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Input: nums = [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

    idea: DFS dynamic programming
    ex = [1, 2, 4, 3]
    we can observe ...
    LIS[0] = 3
    LIS[1] = 2
    LIS[2] = 1
    LIS[3] = 1

    dynamic programming
    start from the lastest LIS[3] = 1 -> (base case) to the front
    LIS[3] = 1
    LIS[2] = max(1 , 1+LIS[3]) -> but 4 is bigger than 3 -> 1
    LIS[1] = max(1, 1+LIS[2], 1+LIS[3]) -> max(1, 2, 2) -> 2
    LIS[0] = max(1, 1+1, 1+1, 1+2) -> 3
    -> time complexity o(n^2)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:


def main():
    n = [3,0,1]
    sol = Solution()
    result = sol.missingNumber(n)
    print(result)
    result = sol.missingNumber2(n)
    print(result)


if __name__ == "__main__":
    main()
