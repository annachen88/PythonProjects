"""
File: LC371_two_sum_of_integer.py
Name: Anna
-------------------------
"""

class Solution:
    """
    ex:
    Input: a = 1, b = 2
    Output: 3
    """
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        # handles overflow
        return (a & mask) if b > 0 else a


def main():
    a = 1
    b = 2
    sol = Solution()
    result = sol.getSum(a,b)
    print(result)


if __name__ == "__main__":
    main()
