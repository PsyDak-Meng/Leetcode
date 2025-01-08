"""
    Reorder Linked List
    Solved 
    You are given the head of a singly linked-list.

    The positions of a linked list of length = 7 for example, can intially be represented as:

    [0, 1, 2, 3, 4, 5, 6]

    Reorder the nodes of the linked list to be in the following order:

    [0, 6, 1, 5, 2, 4, 3]

    Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

    [0, n-1, 1, n-2, 2, n-3, ...]

    You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

    Example 1:

    Input: head = [2,4,6,8]

    Output: [2,8,4,6]
    Example 2:

    Input: head = [2,4,6,8,10]

    Output: [2,10,4,8,6]
    Constraints:

    1 <= Length of the list <= 1000.
    1 <= Node.val <= 1000


    Recommended Time & Space Complexity
    You should aim for a solution with O(n) time and O(1) space, where n is the length of the given list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split linked list: slow fast pointer
        slow, fast = head, head.next
        # slow at linked list mid when fast.next reaches None
        while fast and fast.next: # need fast.next to avoid fast.next.next Nonetype error
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None


        # reverse second half
        while second:
            second_next  = second.next
            second.next = prev
            second = second_next

        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2