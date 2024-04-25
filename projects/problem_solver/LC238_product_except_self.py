"""
File: LC238_product_except_self.py
Name: Anna
-------------------------
238. Product of Array Except Self
Given an integer array nums,
return an array answer such that answer[i] is equal to the product of all
the elements of nums except nums[i].
"""

from typing import List


class Solution:
    """
    ex:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    """
    def product_except_self(self, nums: List[int]) -> List[int]:
        pre = 1
        ans = [1]
        for i in range(len(nums)-1):
            pre *= nums[i]
            ans.append(pre)
        pre = 1
        for i in range(len(ans)-1, -1, -1):  # from end to front
            ans[i] *= pre
            pre *= nums[i]
        return ans


def main():
    nums1 = [1,2,3,4]
    sol = Solution()
    result = sol.product_except_self(nums1)
    print(result)


if __name__ == "__main__":
    main()
