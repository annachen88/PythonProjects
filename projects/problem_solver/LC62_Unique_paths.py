
"""
File: LC62_Unique_paths.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Input: m = 3, n = 2
    Output: 3
    Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
    1. Right -> Down -> Down
    2. Down -> Down -> Right
    3. Down -> Right -> Down

    idea:
    from right bottom side then sum up all the possible path
    """

    def uniquePaths(self, m: int, n: int) -> int:



def main():
    s = "226"
    sol = Solution()
    print(sol.numDecodings(s))


if __name__ == "__main__":
    main()
