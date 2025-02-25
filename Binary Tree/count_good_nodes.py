"""
    Count Good Nodes in Binary Tree
    Solved 
    Within a binary tree, a node x is considered good if the path from the root of the tree to the node x contains no nodes with a value greater than the value of node x

    Given the root of a binary tree root, return the number of good nodes within the tree.

    Example 1:



    Input: root = [2,1,1,3,null,1,5]

    Output: 3


    Example 2:

    Input: root = [1,2,-1,3,4]

    Output: 4
    Constraints:

    1 <= number of nodes in the tree <= 100
    -100 <= Node.val <= 100


    Recommended Time & Space Complexity
    You should aim for a solution with O(n) time andO(n) space, where n is the number of nodes in the given tree.
    """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        count = 0
        stack = [[root, root.val]]

        # keep track [node, prev node cummulated max]
        while stack:
            node, prev_max = stack.pop()

            if node:
                # no prev connecting nodes are larger
                if node.val>=prev_max:
                    count += 1
                
                stack.append([node.left, max(prev_max, node.val)])
                stack.append([node.right, max(prev_max, node.val)])
        
        return count
                
        