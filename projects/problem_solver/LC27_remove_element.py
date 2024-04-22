"""
File: LC27_remove_element.py
Name: Anna
-------------------------
27. Remove element
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.
"""

from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k



def main():
    nums1 = [3, 2, 2, 3]
    m = 3
    sol = Solution()
    result = sol.remove_element(nums1, m)
    print(result)



if __name__ == "__main__":
    main()
