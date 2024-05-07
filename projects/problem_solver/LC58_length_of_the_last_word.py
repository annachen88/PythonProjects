"""
File: LC58_length_of_the_last_word.py
Name: Anna
-------------------------
58. Length of the last word
Given a string s consisting of words and spaces,
return the length of the last word in the string.
"""

from typing import List


class Solution:
    """
    ex:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.
    """
    def lengthOfLastWord(self, s: str) -> int:
        length, pointer = 0, len(s) - 1
        while s[pointer] == ' ':
            pointer -= 1
        while s[pointer] != ' ' and pointer >= 0:
            length += 1
            pointer -= 1
        return length

    def lengthOfLastWord2(self, s: str) -> int:
        return len(s.split()[-1])


def main():
    s = "Hello World"
    sol = Solution()
    print(sol.lengthOfLastWord(s))
    print(sol.lengthOfLastWord2(s))


if __name__ == "__main__":
    main()
