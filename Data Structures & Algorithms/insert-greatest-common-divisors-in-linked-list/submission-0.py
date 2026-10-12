# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(big, small):
            if small > big:
                tmp = big
                big = small
                small = tmp
            if small == 1:
                return 1
            if small == 0:
                return big
            
            big = big % small
            return gcd(small, big)
        
        prev, curr = head, head.next

        while curr:
            new = ListNode(gcd(prev.val, curr.val))
            prev.next = new
            new.next= curr
            prev = curr
            curr = curr.next
        
        return head


