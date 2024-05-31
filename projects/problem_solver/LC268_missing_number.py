"""
File: LC268_missing_number.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Counting Bits - Dynamic Programming
    ex:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

    """


    def missingNumber(self, nums: List[int]) -> int:
        input_total = (1 + len(nums)) * len(nums) // 2
        # print(input_total)
        for i in range(len(nums)):
            input_total -= nums[i]
        return input_total


    def missingNumber2(self, nums: List[int]) -> int:
        result = len(nums)
        for i in range(len(nums)):
            result += (i - nums[i])
        return result
    """
    n -> [0-3 , 1-0, 2-1] ,total = -1
    -1 + 3 = 2
    因正常：[0,1,2]
    異常  :[3,0,1]
    """


def main():
    n = [3,0,1]
    sol = Solution()
    result = sol.missingNumber(n)
    print(result)
    result = sol.missingNumber2(n)
    print(result)


if __name__ == "__main__":
    main()
