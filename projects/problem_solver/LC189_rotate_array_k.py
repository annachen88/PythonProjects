"""
File: LC189_rotate_array.py
Name: Anna
-------------------------
189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

from typing import List


class Solution:
    """
    ex:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#       if null return null
        if not nums:
            return

#       rotate k
        k = k % len(nums)
        self.reverse(0, len(nums)-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums)-1, nums)

    def reverse(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1


def main():
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    sol.rotate(nums1, 3)
    print(nums1)


if __name__ == "__main__":
    main()
