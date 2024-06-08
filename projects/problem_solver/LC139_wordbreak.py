"""
File: LC139_wordbreak.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    idea 1 : o(n * m)
    find the first fit string, then split the string find another matched string ...

    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:



def main():
    text1 = "abcde"
    text2 = "ace"
    sol = Solution()
    result = sol.longestCommonSubsequence(text1, text2)
    print(result)


if __name__ == "__main__":
    main()
