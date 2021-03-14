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
    
    # Leetcode 142 环形链表找到其尾部连接到的节点索引
    # 双指针: 链表题一般都是双指针解决的, 例如找到距离尾部的第k个节点, 寻找环入口, 寻找公共尾部入口
    # fast, slow 指向 head, 每轮: fast走2步, slow走1步
    # 1.双指针第一次相遇：
    #   1.第一种结果：fast走完链表, 说明链表无环, 直接返回None
    #   2.第二种结果：if fast == slow:
    #       假设链表共有a + b个节点, 头部到环入口有 a 个节点, 链表环有 b 个节点, 两指针分别走了 f, s 步, 则有：
    #           1.f = 2 * s;
    #           2.fast 比 slow 多走了n个环的长度, f = s + n * b;
    #       1式与2式相减得 f = 2 * n * b, s = n * b, 即 fast 和 slow 分别走了 2n, n 个环的周长
    # 2.分析:
    #   1.指针从链表头部一直向前走并统计步数k: k = a + n * b
    #   2.s = n * b, 那么此时只要让 slow 再走 a 步停下来就可以到达环的入口
    #   3.如何求 a ? 还是双指针, 另一个指针从 head 出发, 与 slow 一起向前走 a 步, 两者在入口节点重合。
    # 3.双指针第二次相遇:
    #   1.slow指针不动, 将 fast 指针重新指向 head; 此时 f = 0, s = n * b; 每轮: slow 和 fast 同时走1步;
    #   2.当 f = a 时, s = a + n * b, 此时两指针重合, 同时指向链表环入口
    # 4. 返回 slow 指针指向的节点
    def detectcycle_and_findconnect(self, head:ListNode):
        fast, slow = head, head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                a = 0
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                    a += 1
                return slow
        return None
