"""
File: LC33_search_in_rotated_sorted_array.py
Name: Anna
"""
from typing import List


class Solution:
    """
    33. Search in Rotated Sorted Array
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    ------------------------------------------
    idea : binary search
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # left part
            # if nums[left] < nums[mid]:
                





def main():
    nums = [4,5,6,7,0,1,2]
    sol = Solution()
    result = sol.search(nums,0)
    print(result)


if __name__ == "__main__":
    main()