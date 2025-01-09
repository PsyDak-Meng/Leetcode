"""
    Remove Node From End of Linked List
    Solved 
    You are given the beginning of a linked list head, and an integer n.

    Remove the nth node from the end of the list and return the beginning of the list.

    Example 1:

    Input: head = [1,2,3,4], n = 2

    Output: [1,2,4]
    Example 2:

    Input: head = [5], n = 1

    Output: []
    Example 3:

    Input: head = [1,2], n = 2

    Output: [2]
    Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz


    Recommended Time & Space Complexity
    You should aim for a solution with O(N) time and O(1) space, where N is the length of the given list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       # Two pter: move right pointer to n-th node
       dummy = ListNode(0, head)
       left, right = dummy, head # left is at dummy to skip pointer from (N-n-1)->(N-n+1) to pop (N-n)th

       for _ in range(n):
           right = right.next

       # move two pters to the wight most end
       while right:
           left = left.next # left is at the (N-n-1)th
           right = right.next
       
       # pop n-th node
       left.next = left.next.next

       return dummy

