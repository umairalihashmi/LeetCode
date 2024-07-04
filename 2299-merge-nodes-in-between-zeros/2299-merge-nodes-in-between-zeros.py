# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        start = dummy = ListNode(0)
        s = 0

        while head:
            if not head.val:
                dummy.val = s
                s = 0
                dummy.next = ListNode(0)
                last = dummy
                dummy = dummy.next
            else:
                s+=head.val
            head = head.next
        last.next = None
        return start.next
        