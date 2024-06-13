
"""
File: LC91_decode_ways.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    encode from 1 ~ 26
    Input: s = "226"
    Output: 3
    Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

    Input: s = "06"
    Output: 0
    Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
    """

    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}   # save the length, for checking

        # idea : dfs[i] = dfs[i+1] + dfs[i+2] -> if 226 then can be possible 2 or 26
        def dfs(i):
            if i in dp:
                return dp[i]  # 表示最後一個
            if s[i] == "0":
                return 0  # can't start from the zero
            res = dfs(i+1)  # keep going
            # check can contains next character between 10~26
            if (i+i < len(s)
                    and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res  # save the decode
            return res

        return dfs(0)  # start from the s[0]


def main():
    s = "226"
    sol = Solution()
    print(sol.numDecodings(s))


if __name__ == "__main__":
    main()
