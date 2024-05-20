"""
File: LC152_Maximum_Product_Subarray.py
Name: Anna
"""
from typing import List


class Solution:
    """
    152. Maximum Product Subarray
    HINT : all positive, all negative, 0(not in consideration -> do not add in the list)
    ex:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    idea:
    [2,3,-2,4]
    start from default max, min = 1,1
    trace1 : 1*2, 1*2 = 2, 2 => max = 2, min =2
    trace2 : 2*3, 2*3 => 6, 6 => (( max = 6 )), min =3
    trace3 : 6*-2, 2*-2=> -12, -6 => max = -2, min = -12
    trace4 : -2*4, -12*4 => -8, -48 => max=4, min = -48
    """

    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMin , curMax = 1, 1
        for i in nums:
            temp = curMax * i
            temp2 = curMin * i
            curMin = min(temp, temp2, i)  #[-1, 8, 8]
            curMax = max(temp, temp2, i)
            result = max(result, curMax)
        return result


def main():
    nums = [2,3,-2,4]
    sol = Solution()
    result = sol.maxProduct(nums)
    print(result)


if __name__ == "__main__":
    main()