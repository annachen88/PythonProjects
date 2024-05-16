"""
File: LC53_MaximumSubarray.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    HINT : Sliding windows
    ex:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
            # print(maxSub,curSum)
        return maxSub

    """
    trace 1: maxSub = -2, curSum = 0
    trace 2: maxSub = -2, curSum = -2
    trace 3: maxSub = 1, curSum = 1
    trace 4: maxSub = 1, curSum = -2
    trace 5: maxSub = 4, curSum = 4
    trace 6: maxSub = 4, curSum = 3
    trace 7: maxSub = 5, curSum = 5
    trace 8: maxSub = 6, curSum = 6
    trace 9: maxSub = 6, curSum = 1
    trace 10: maxSub = 6, curSum = 5
    """

def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print(result)


if __name__ == "__main__":
    main()
