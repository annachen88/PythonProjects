
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
    [1] value from [3] + [4]
    [1][3]
    [4]
    """

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]



def main():
    # s = "226"
    sol = Solution()
    print(sol.uniquePaths(3,2))


if __name__ == "__main__":
    main()
