"""
File: LC134_gas_station.py
Name: Anna
-------------------------
134. Gas Station
Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction, otherwise return -1
從一點出發，如果當前的gas值大於cost值，就可以繼續前進，
此時到下一個站點，剩餘的gas加上當前的gas再減去cost，看是否大於0，若大於0，則繼續前進。
"""

from typing import List


class Solution:
    """
    ex:
    Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
    Output: 3
    Explanation:
    Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
    Travel to station 4. Your tank = 4 - 1 + 5 = 8
    Travel to station 0. Your tank = 8 - 2 + 1 = 7
    Travel to station 1. Your tank = 7 - 3 + 2 = 6
    Travel to station 2. Your tank = 6 - 4 + 3 = 5
    Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
    Therefore, return 3 as the starting index.
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start, total = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start += 1
        return start


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    sol = Solution()
    sol.canCompleteCircuit(gas, cost)
    print(sol.canCompleteCircuit(gas, cost))


if __name__ == "__main__":
    main()
