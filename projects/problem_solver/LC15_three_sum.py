"""
File: LC15_three_sum.py
Name: Anna
"""
from typing import List


class Solution:
    """
    15. Three Sum
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.
    ------------------------------------------
    HINT :
        1. sort
        2. skip the same element
        3. using left and right pointer
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 排序
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  # 重複則不比
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                three_sum = a + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    # find three sum
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    if nums[left] == nums[left-1] and left < right:
                        left += 1
        return result


def main():
    nums = [-1,0,1,2,-1,-4]
    sol = Solution()
    result = sol.threeSum(nums)
    print(result)


if __name__ == "__main__":
    main()