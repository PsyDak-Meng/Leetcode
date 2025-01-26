"""
    Kth Smallest Integer in BST
    Solved 
    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

    A binary search tree satisfies the following constraints:

    The left subtree of every node contains only nodes with keys less than the node's key.
    The right subtree of every node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees are also binary search trees.
    Example 1:



    Input: root = [2,1,3], k = 1

    Output: 1
    Example 2:



    Input: root = [4,3,5,2,null], k = 4

    Output: 5
    Constraints:

    1 <= k <= The number of nodes in the tree <= 1000.
    0 <= Node.val <= 1000


    Recommended Time & Space Complexity
    You should aim for a solution as good or better than O(n) time and O(n) space, where n is the number of nodes in the given tree.
    """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []

        # DFS
            # Each level are binary search trees (all left<node<all right)
            # Traverse and add to ordered list in order of <left sub tree, node, right sub tree>
        def dfs(node):
            nonlocal nums

            if node.left:
                dfs(node.left)
            
            # append node value in the middle
            # leaf node appended without left & right sub trees
            nums.append(node.val)

            if node.right:
                dfs(node.right)
        
        dfs(root)
        return nums[k-1]
            
            

        