"""
    Valid Binary Search Tree
    Solved 
    Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

    A valid binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.
    Example 1:



    Input: root = [2,1,3]

    Output: true
    Example 2:



    Input: root = [1,2,3]

    Output: false
    Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.

    Constraints:

    1 <= The number of nodes in the tree <= 1000.
    -1000 <= Node.val <= 1000


    Recommended Time & Space Complexity
    You should aim for a solution with O(n) time and O(n) space, where n is the number of nodes in the given tree.
    """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # cannot direct DFS due to null pointers
        # keep track of each node and its lower & upper bound:
        def valid(node, low, up):
            if not node:
                return True
            
            val = node.val

            # if not within range, false
            if not low<val<up:
                return False
            # if in range, check left & right sub tree: 
            else:
                # left subtree's only restraint is be lower than node: current lower bound < left < current node
                # right subtree's only restraint is be above node: current node < left < current upeer bound
                return valid(node.left, low, val) and valid(node.right, val, up)
            
        return valid(root, float('-inf'), float('inf'))