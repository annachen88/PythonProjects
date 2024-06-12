
"""
File: LC213_house_robberII.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Given a circular array (the first element and the last element are equal),
    so we find the max sum from  nums[0], nums[1:] -> not include the first, nums[:-1] -> not include the last
    Input: nums = [2,3,2]
    Output: 3
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

    Input: nums = [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4.

    """
    # find the max sum without the neighborhood
    def rob(self, nums: List[int]) -> int:

        # find the max between, first element, without first element array, without latest element array
        return  max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

    def rob_helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


def main():
    nums = [1,2,3,1]
    sol = Solution()
    # sol.rob(nums)
    print(sol.rob(nums))


if __name__ == "__main__":
    main()
