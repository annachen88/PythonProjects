"""
File: LC01_twosum.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    ex:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return


def main():
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    result = sol.twoSum(nums,target)
    print(result)


if __name__ == "__main__":
    main()
