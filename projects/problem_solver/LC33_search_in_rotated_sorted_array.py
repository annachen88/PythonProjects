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
    idea: binary search

    trace 0: [4,5,6,7,0,1,2] => 0, 3, 6
    trace 1: [0,1,3] => 4, 5, 6
    trace 3: [0] => 4, 4, 4
    """

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] == target:
                return mid

            # left part
            if nums[left] < nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    # 左半的右邊
                    left = mid + 1
                else:
                    # 左半的左邊
                    right = mid - 1
            # right part
            else:
                if nums[mid] > target or target > nums[right]:
                    # 右半的左邊
                    right = mid - 1
                else:
                    # 右半的右邊
                    left = mid + 1
        return mid


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    result = sol.search(nums,0)
    print(result)


if __name__ == "__main__":
    main()
