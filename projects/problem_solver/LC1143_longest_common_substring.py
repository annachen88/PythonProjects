"""
File: LC1143_longest_common_substring.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Input: text1 = "abcde", text2 = "ace"
    Output: 3
    Explanation: The longest common subsequence is "ace" and its length is 3.
    idea : iterate the text then if text1[i] = text2[j] = 1 + (右下角) , else = max(neighbor value)
    2D graph:
         [a b c d e]
        a
        c
        e         (o) <- start from the bottom
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # set the default 2D array
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        # from the rightest
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    # 1 + (右下角)
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # 右,下
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


def main():
    text1 = "abcde"
    text2 = "ace"
    sol = Solution()
    result = sol.longestCommonSubsequence(text1, text2)
    print(result)


if __name__ == "__main__":
    main()
