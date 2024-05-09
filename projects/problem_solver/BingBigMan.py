"""
File: BingBigMan.py
Name: Anna
-------------------------
Description :LC70_climbing stairs
Bing一次只能走一層、兩層樓梯。舉例來說,若是辦公室距離地面三層樓梯,
則Bing可以有三種方法(1, 1, 1)、(2, 1)、(1, 2)可以走到辦公室。
"""

from typing import List


def climb_stairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# recursive many cache
def count_ways(num: int) -> int:
    if num <= 1:
        return 1
    else:
        return count_ways(num-1) + count_ways(num-2)


# O(n)
"""
idea: BOTTOM UP DYNAMIC PROGRAMMING : TWO DECISION EACH TIME
ex : 5
                    0
                /       \
               1          2
            /   \        /  \
          2      3      3     4
         / \     /\    / \   / \
        3   4   4  5  4  5   5  X
       /\   /\  /\    /\
      4 (5)(5)X(5)X (5)X
     /\
    (5) X
--------------------------------------
FROM 5-0 :  0   1   2   3   4   5
WAYS        8   5   3   2   1   1
           5+3 3+2 2+1 1+1
"""
def climbStairs(num: int) -> int:
    one, two = 1, 1
    for i in range(num-1):
        result = one
        one = one + two
        two = result
    return one


def main():
    print(count_ways(5))
    print(climb_stairs(5))
    print(climbStairs(5))


if __name__ == "__main__":
    main()
