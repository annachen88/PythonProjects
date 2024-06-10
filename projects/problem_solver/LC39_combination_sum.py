"""
File: LC39_combination_sum.py
Name: Anna
-------------------------
"""

from typing import List


class Solution:
    """
    Input: candidates = [2,3,6,7], target = 7
    Output: [[2,2,3],[7]]
    Explanation:
    2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    7 is a candidate, and 7 = 7.
    These are the only two combinations.

    idea :
        beacase can contain the same element
        so make a decision tree, the left tree is contain and the right is not contain
        for example :
                *
               / \
            [2]   []
          /    \
        [2,2]  [2]
              /   \
           [2,3] [2,6]
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur_list, total):
            if total == target:  # get the result and copy the list to the result array
                res.append(cur_list.copy())
                return
            if total > target or i >= len(candidates):  # decision tree stop
                return
            # keep going
            # the left tree
            cur_list.append(candidates[i])
            dfs(i, cur_list, total + candidates[i])
            # the right tree without candidates[i] so pop it from the cur_list
            cur_list.pop()
            # keep going to the next element
            dfs(i+1, cur_list, total)

        # start from 0 and empty list
        dfs(0, [], 0)
        return res


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    print(sol.combinationSum(candidates, target))


if __name__ == "__main__":
    main()
