"""
File: LC191_number_of_1_bits.py
Name: Anna
-------------------------
"""

class Solution:
    """
    ex:
    Input: n = 11
    Output: 3
    Explanation:
    The input binary string 1011 has a total of three set bits.
    """

    # if input n = 2147483645 (1111111111111111111111111111101) then need to run 32 times
    # (time complexity)
    def hammingWeight(self, n: int) -> int:
        total_count = 0
        while n:  # n > 0
            total_count += n % 2
            n = n >> 1  # shift 1 to the right -> 101 -> 10
        return total_count


def main():
    a = 2147483645
    # b = 2
    sol = Solution()
    result = sol.hammingWeight(a)
    print(result)


if __name__ == "__main__":
    main()
