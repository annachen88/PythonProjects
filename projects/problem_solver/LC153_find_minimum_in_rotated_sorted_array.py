"""
File: LC153_find_minimum_in_rotated_sorted_array
Name: Anna
"""
from typing import List


class Solution:
    """
    153. Find Minimum in Rotated Sorted Array
    HINT : sorted array, using medium pointer
    Input: nums = [3,4,5,1,2]
    Output: 1
    Explanation: The original array was [1,2,3,4,5] rotated 3 times.
    idea:
        if nums[medium] >= nums[left]:
           search right
        else:
            search left
    """

    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
            # 找Ｍedium
            mid = (left + right) // 2
            result = min(result, nums[mid])
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid -1
        return result


def main():
    nums = [3,4,5,1,2]
    sol = Solution()
    result = sol.findMin(nums)
    print(result)


if __name__ == "__main__":
    main()