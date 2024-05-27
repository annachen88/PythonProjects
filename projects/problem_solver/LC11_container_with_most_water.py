"""
File: LC11_container_with_most_water.py
11. Container With Most Water
Name: Anna
-------------------------
"""
from typing import List


class Solution:
    """
    找區間內Area最大的
    ex:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented
    by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    """

    # liner time solution
    # using two pointer then replace the max area
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right-left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    # brute force
    def maxArea2(self, height: List[int]) -> int:
        max_area = 0
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r-l) * min(height[l],height[r])
                max_area = max(max_area, area)
        return max_area


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    result = sol.maxArea(height)
    print(result)
    result = sol.maxArea2(height)
    print(result)


if __name__ == "__main__":
    main()
