"""
File: LC55_jump_game.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    ex:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    idea 1: brute decision tree
    idea 2: greedy
            from the goal index to the first index, check if it can reach
    """

    def canJump(self, nums: List[int]) -> bool:
        pass


def main():
    nums = [3, 2, 1, 0, 4]
    sol = Solution()
    result = sol.canJump(nums)
    print(result)


if __name__ == "__main__":
    main()
