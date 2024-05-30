"""
File: LC338_counting_bits.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Counting Bits - Dynamic Programming
    ex:
    Input: n = 5
    Output: [0,1,1,2,1,2]
    Explanation: 4 個一規律
        0 --> 0000
        1 --> 0001
        2 --> 0010
        3 --> 0011
        ----------------- offset = [1, 2, 4, 8, 16]
        4 --> 0100  --> 1 + dp[n-4]
        5 --> 0101  --> 1 + dp[n-4]
        .
        .
        .
        8 --> 1000 --> 1 + dp[n-8]
    """
    def countBits(self, n: int) -> List[int]:
        pass

def main():
    a = 2147483645
    sol = Solution()
    result = sol.hammingWeight(a)
    print(result)
    result = sol.hammingWeight2(a)
    print(result)


if __name__ == "__main__":
    main()
