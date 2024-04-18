"""
File: LC88_merge_sorted_array.py
Name: Anna
-------------------------
88. Merge Sorted Array
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m + n - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[k] = nums2[n]
                n -= 1
                k -= 1
            else:
                nums1[k] = nums1[m]
                m -= 1
                k -= 1
        while n >= 0:
            nums1[k] = nums2[n]
            n -= 1
            k -= 1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == "__main__":
    main()
