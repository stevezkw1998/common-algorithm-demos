from datastructure.LinkedList import LinkedList, ListNode

def reverse(head:ListNode):  # 尾插法
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

def reverse2(head, tail):
    prev = tail.next
    p = head
    while prev != tail:
        next = p.next
        p.next = prev
        prev = p
        p = next
    tail, head

# 反转位置m到n的链表, 只扫描一趟
# 如果用切段 reverse 法, 需扫描两遍, 所以这里用delete, insert法
# 在 left 和 right 之间, 每遍历一个node就move到pre后一位的位置
def reversebetween(head:ListNode, left, right):
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    for i in range(left-1):
        pre = pre.next
    cur = pre.next
    for i in range(right-left):
        next = cur.next
        cur.next = next.next
        next.next = pre.next
        pre.next = next
    return dummy.next

# k个一组反转链表
# 时间复杂度O(n), 空间复杂度O(1)
def reversekgroup(head:ListNode, k):
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    while head:
        tail = pre
        for i in range(k):
            tail = tail.next
            if not tail:
                return dummy.next
        next = tail.next
        tail.next = None
        head, tail = reverse2(head, tail)
        pre.next = head
        tail.next = next # 切断反转性能更好
        pre = tail
        head = tail.next
    return dummy.next