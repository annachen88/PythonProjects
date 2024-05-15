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
    ---------------------------------------
    sol 1: time complexity O(n), but take O(n) memory space complexity
    nums = [1,2,3,4]
    pre = [1, 2, 6, 24] = i 前面相乘結果
    post = [24, 24, 12, 4] = i 後面相乘結果
    result = [pre[i-1]*post[i+1]] -> if not exist-> default 1
    result: [24,12,8,6] = [1*24, 1*12, 2*4, 6*1]
    ---------------------------------------
    sol 2: time complexity O(n), memory space complexity O(1)
    nums = [1,2,3,4]
    idea :
        start from the beginning(i) using prefix variable(default 1) then record into the result array
            record array position -> i+1
        start from the end(len(nums)) using postfix variable(default 1) then postfix(i) multiply position(i+1) into the
        result array
            record array position -> i = len(len(nums))

    Trace the running process
    nums = [1,2,3,4]
    result = []
    start from the beginning -> result = [1, 1, 2, 6]
    trace 0: given default prefix = 1
    trace 1: prefix = 1, result = [1], update prefix = 1 (result[0])
    trace 2: prefix = 1, result = [1, 1*1] = [1,1] = [prefix * nums[0]], update prefix = 1 (result[1])
    trace 3: prefix = 1, result = [1, 1, 1*2] =  [prefix * nums[1]], update prefix = 2 (result[2])
    trace 4: prefix = 2, result = [1, 1, 2, 2*3] =  [prefix * nums[2]], update prefix = 6 (result[3])
    then start from the ending to the beginning
    trace 5: given default postfix =1
    trace 6: postfix =1, result = [1, 1, 2, 2*3*1] = [1, 1, 2, 6] = result[3]*postfix ,update postfix = 4( postfix * nums[3])
    trace 7: postfix =4, result = [1, 1, 2*4, 6] = [1, 1, 8, 6] = result[2]*postfix, update postfix = 12 ( postfix * nums[2])
    trace 8: postfix =12, result = [1, 1*12, 8, 6] = [1, 12, 8, 6] =result[1]*postfix, update postfix = 24 ( postfix * nums[1])
    trace 9: postfix = 24, result = [1*24, 12, 8, 6] = result[0]*postfix ...
    finish then return result
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
