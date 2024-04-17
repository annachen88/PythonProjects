"""
File: LC219_contains_nearby_duplicate.py
Name: Anna
-------------------------
219. Contains Duplicate II
Given an integer array nums and an integer k, return true
if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
from collections import defaultdict
from typing import List


def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    d = defaultdict(int)
    for i in range(len(nums)):
        d[nums[i]] += 1
        if d[nums[i]] > 1:
            for j in range(i-1, i-k-1, -1):
                if j >= 0 and nums[i] == nums[j]:
                    return True
            d[nums[i]] = 1
    return False


def main():
    print(contains_nearby_duplicate([1, 2, 3, 1], 3))


if __name__ == "__main__":
    main()
