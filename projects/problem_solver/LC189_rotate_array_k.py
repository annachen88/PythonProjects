"""
File: LC189_rotate_array_k.py
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

        # rotate k
        # [1, 2, 3, 4, 5, 6, 7]
        k = k % len(nums)
        # [1, 2, 3, 4, 5, 6, 7]
        self.reverse(0, len(nums)-1, nums)
        # [7, 6, 5, 4, 3, 2, 1]
        self.reverse(0, k-1, nums)
        # [5, 6, 7, 4, 3, 2, 1]
        self.reverse(k, len(nums)-1, nums)
        # [5, 6, 7, 1, 2, 3, 4]

    def reverse(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    def reverse2(self, array, k):
        if k > len(array):
            k = k % len(array)
        # array[0:] : [1, 2, 3, 4, 5, 6, 7]
        # array[len(array) - k:] : [5, 6, 7]
        # -> [5, 6, 7, 4, 5, 6, 7]
        # array[k:] :  [4, 5, 6, 7]
        # array[0:len(array) - k] : [1, 2, 3, 4]
        # -> [5, 6, 7, 1, 2, 3, 4]
        array[0:], array[k:] = array[len(array) - k:], array[0:len(array) - k]
        return array

def main():
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    nums2 = [1, 2, 3, 4, 5, 6, 7]
    sol = Solution()
    sol.rotate(nums1, 3)
    print(nums1)
    sol.reverse2(nums2, 3)
    print(nums2)


if __name__ == "__main__":
    main()
