"""
    Subtree of Another Tree
    Solved 
    Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

    Example 1:



    Input: root = [1,2,3,4,5], subRoot = [2,4,5]

    Output: true
    Example 2:



    Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

    Output: false
    Constraints:

    0 <= The number of nodes in both trees <= 100.
    -100 <= root.val, subRoot.val <= 100


    Recommended Time & Space Complexity
    You should aim for a solution as good or better than O(m * n) time and O(m + n) space, where n and m are the number of nodes in root and subRoot, respectively.
    """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Recursive check if is subtree
        if not root:
            return False
        if not subRoot:
            return True
        
        if self.sameTree(root,subRoot):
            return True
        # one of leaf node is subTree will satisfy
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    # recursive check same tree
    def sameTree(self, root, subTree):
        if not root and not subTree:
            return True

        # both root and subTree cannot be and node
        if root and subTree and root.val==subTree.val:
            # both leaf node has to be the same to satisfy
            return self.sameTree(root.left, subTree.left) and self.sameTree(root.right, subTree.right)

        return False


