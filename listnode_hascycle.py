from datastructure.LinkedList import LinkedList, ListNode

class Solution:
    def hascycle(self, head:ListNode):
        p_fast = head
        p_slow = head
        while p_fast and p_slow.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            if p_fast == p_slow:
                return True
        return False