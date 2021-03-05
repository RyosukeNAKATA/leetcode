"""
Question.
Write a program to find the node at which the intersection of two singly linked lists begins.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dict = {}
        while headA:
            dict[headA]=1
            headA = headA.next
        while headB:
            if headB in dict:
                return headB
            headB = headB.next
        return None