"""
File: LC190_reverse_bits.py
Name: Anna
-------------------------
"""
from typing import List


class Solution:
    """
    Reverse Bits - Binary
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
    Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned
    integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

    idea:
    ex : 1011 -> 1101, result =''
    step 0 : shift right 0 & 1 -> 1011 & 1111 -> 1011 -> 1
            and shift left (31-0) --> 1000
    step 1 : shift right 1 & 1 -> 011 & 1111 -> 0101 ->
            and shift left (31-1) --> 0100
    step 2 : shift right 2 & 1 -> 0010 & 1111 -> 0010
            and shift left (31-2)
    result = '1101'
    """

    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1
            result = result | (bit << (31 - i ))
        return result



def main():
    n = 10100101000001111010011100
    sol = Solution()
    result = sol.reverseBits(n)
    print(result)


if __name__ == "__main__":
    main()
