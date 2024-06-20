"""
File: LC133_clone_graph.py
Name: Anna
-------------------------
"""

from typing import List
from typing import Optional
""""
    Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
    Output: [[2,4],[1,3],[2,4],[1,3]]
    Explanation: There are 4 nodes in the graph.
    1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
    4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
    
    Input: adjList = [[]]
    Output: [[]]
    Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:

    # idea : Depth First Search
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyNewGraph = {}
        def dfs(node):
            if node in copyNewGraph:
                return copyNewGraph[node]

            copy = Node(node.val)
            copyNewGraph[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


def main():
    # adjList = [[2,4],[1,3],[2,4],[1,3]]
    adjList = Node(1)
    sol = Solution()
    sol.cloneGraph(adjList)



if __name__ == "__main__":
    main()
