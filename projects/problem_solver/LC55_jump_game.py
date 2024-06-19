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

    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

    idea 1: brute decision tree -> time complexity O(n^n)
    idea 2: greedy -> time complexity O(n)
            from the goal index to the first index, check if it can reach

    """

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1,-1,-1): # from last
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False


def main():
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    sol = Solution()
    result = sol.canJump(nums1)
    print(result)
    result = sol.canJump(nums2)
    print(result)


if __name__ == "__main__":
    main()
