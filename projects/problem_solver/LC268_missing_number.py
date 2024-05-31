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
        print(input_total)
        for i in range(len(nums)):
            input_total -= nums[i]
        return input_total


def main():
    n = [3,0,1]
    sol = Solution()
    result = sol.missingNumber(n)
    print(result)



if __name__ == "__main__":
    main()
