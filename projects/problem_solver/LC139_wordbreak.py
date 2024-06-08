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
    iterate the dictionary
    find the first fit string, then split the string find another matched string ...
    from the last character
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # initial dynnamic programming array
        dp = [False] * (len(s) + 1)     # default False
        dp[len(s)] = True
        for i in range(len(s) -1, -1, -1):  # from the last character
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i] + dp[i + len(w)]
                if dp[i]:
                    break  # do not keep because it must contain
        return dp[0]


def main():
    text1 = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    print(sol.wordBreak(text1, wordDict))


if __name__ == "__main__":
    main()
