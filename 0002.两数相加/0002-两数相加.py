# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toNum(l: ListNode):
            listnum = []
            while l != None:
                listnum.append(str(l.val))
                l = l.next
            return int(''.join(reversed(listnum)))

        def toListNode(n: str):
            l = ListNode(int(n[len(n)-1]))
            l_tail = l
            for j in range(1,len(n)):
                l_tail.next = ListNode(int(n[len(n)-1-j]))
                l_tail = l_tail.next
            return l
        return toListNode(str(toNum(l1) + toNum(l2)))