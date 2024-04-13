# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        visited = {}
        temp = headA
        while temp:
            visited[temp] = 1
            temp = temp.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next

        return None
        
