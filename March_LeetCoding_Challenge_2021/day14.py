"""
Question: Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.
Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
Constraints:
- The number of nodes in the list is n.
- 1 <= k <= n <= 105
- 0 <= Node.val <= 100
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        def listnode_to_pylist(listnode):
            ret = []
            while True:
                ret.append(listnode.val)
                if listnode.next != None:
                    listnode = listnode.next
                else:
                    return ret

        def pylist_to_listnode(pylist, link_count):
            if len(pylist) > 1:
                ret = precompiled.listnode.ListNode(pylist.pop())
                ret.next = pylist_to_listnode(pylist, link_count)
                return ret
            else:
                return precompiled.listnode.ListNode(pylist.pop(), None)
        
        pylist = listnode_to_pylist(head)
        pylist[k-1], pylist[-k] = pylist[-k], pylist[k-1]
        l = len(pylist)
        node = pylist_to_listnode(pylist[::-1], l)
        return node