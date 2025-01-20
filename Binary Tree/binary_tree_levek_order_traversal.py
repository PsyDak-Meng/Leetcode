"""
    Binary Tree Level Order Traversal
    Solved 
    Given a binary tree root, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

    Example 1:



    Input: root = [1,2,3,4,5,6,7]

    Output: [[1],[2,3],[4,5,6,7]]
    Example 2:

    Input: root = [1]

    Output: [[1]]
    Example 3:

    Input: root = []

    Output: []
    Constraints:

    0 <= The number of nodes in both trees <= 1000.
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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        if not root:
            return []

        # use queue FIFO
        queue = [[root,1]]
        node_list = []

        while queue:
            node, level = queue.pop(0)
            if node:
                node_list.append([node.val, level])
                queue.append([node.left, level+1])
                queue.append([node.right, level+1])

        # split up list
        result = []
        node_group = []
        current_level = 1

        for node in node_list:
            # keep clusteting same level node if level didn't change
            if node[1] == current_level:
                node_group.append(node[0])
            # add cluster to result & reset cluster & move up level
            if node[1] != current_level:
                result.append(node_group)
                node_group = [node[0]]
                current_level += 1
        # complement cluster
        result.append(node_group)

        return result

        