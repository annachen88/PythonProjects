
"""
File: LC198_house_robber.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    idea :
        for each num, get max of prev subarr,
        or num + prev sub array not including last element, store results of prev, and prev not including last element

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.
    """


    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(rob1 + n , rob2)
            rob1 = rob2
            rob2 = temp
            print(rob1, rob2, temp)
        return rob2


def main():
    nums = [1,2,3,1]
    sol = Solution()
    sol.rob(nums)
    # print(sol.rob(nums))


if __name__ == "__main__":
    main()
