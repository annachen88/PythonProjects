"""
File: LC217_contains_duplicate.py
Name: Anna
-------------------------
217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

from typing import List


class Solution:
    """
    sol 1 : brute way loop the array
    sol 2 : sort the array and compare the neighbor
    sol 3 : with HashSet
    Input: nums = [1,2,3,1]
    Output: true
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


def main():
    nums = [1, 2, 3, 1]
    sol = Solution()
    result = sol.containsDuplicate(nums)
    print(result)


if __name__ == "__main__":
    main()
