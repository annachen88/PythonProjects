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
    ***(1)*** start from the lastest LIS[3] = 1 -> (base case) to the front
    LIS[3] = 1
    LIS[2] = max(1 , 1+LIS[3] ***(2)*** ) -> ***(3)*** but 4 is bigger than 3 -> 1
    LIS[1] = max(1, 1+LIS[2], 1+LIS[3]) -> max(1, 2, 2) -> 2
    LIS[0] = max(1, 1+1, 1+1, 1+2) -> 3
    -> time complexity o(n^2)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):  # from the end ***(1)***
            for j in range(i+1,len(nums)):  # get the i+1 ~ to the end ***(2)***
                if nums[i] < nums[j]:  # ***(3)***
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


def main():
    n = [1, 2, 4, 3]
    sol = Solution()
    result = sol.lengthOfLIS(n)
    print(result)


if __name__ == "__main__":
    main()
