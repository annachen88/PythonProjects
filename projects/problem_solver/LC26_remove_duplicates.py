"""
File: LC26_remove_duplicates.py
Name: Anna
-------------------------
26. Remove Duplicates from Sorted Array
Given an integer array nums sorted in non-decreasing order,
 remove the duplicates in-place such that each unique element appears only once.
 The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.
"""

from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        start, end, k = 0, 0, 0
        # k : 第幾個沒重複的
        while end < len(nums):
            if nums[start] == nums[end]:
                end += 1
            else:
                nums[k] = nums[start]
                start = end
                k += 1
        nums[k] = nums[start]
        return k + 1

    def remove_duplicates2(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


def main():
    nums1 = [1, 1, 2]
    nums2 = [1, 1, 2]
    sol = Solution()
    sol.remove_duplicates(nums1)
    print(nums1)
    sol.remove_duplicates2(nums2)
    print(nums2)


if __name__ == "__main__":
    main()
