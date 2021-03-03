class ListNode:         # 链表中的结点
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:       # 链表类
    def __init__(self):
        self.head = None

    def size(self):     # size() —— 返回链表中数据元素的个数/链表长度
        size = 0
        head = self.head
        while head:
            size += 1
            head = head.next
        return size
    
    def empty(self):    # empty() —— 若链表为空则返回一个布尔值 true
        return True if self.head else False

    def value_at(self, index):      # value_at(index) —— 返回第 n 个元素的值（从0开始计算），若索引超过链表长度则报错
        if not self.head:
            raise IndexError("Index out of range.")
        head = self.head
        while index > 0:
            if not head:
                raise IndexError("Index out of range.")
            head = head.next
            index -= 1
        return head.val

    def add(self, value):   # add(value) —— 添加元素到链表的首部
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def popleft(self):    # popleft() —— 删除首部元素并返回其值，若链表为空则报错
        if not self.head:
            raise IndexError("Pop from empty list")
        value = self.head.val
        self.head = self.head.next
        return value

    def append(self, value):    # append(value) —— 添加元素到链表的尾部
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        head = self.head
        while head.next:
            head = head.next
        head.next = new_node

    def pop(self):              # pop() —— 删除尾部元素并返回其值，若链表为空则报错
        if not self.head:
            raise IndexError("Pop from empty list")
        if not self.head.next:
            value = self.head.val
            self.head = None
            return value
        head = self.head
        while head.next.next:
            head = head.next
        value = head.next.val
        head.next = None
        return value

    def front(self):            # front() —— 返回首部元素的值，若链表为空则报错
        if not self.head:
            raise ValueError("Linked list is empty")
        return self.head.val

    def back(self):             # back() —— 返回尾部元素的值，若链表为空则报错
        if not self.head:
            raise ValueError("Linked list is empty")
        head = self.head
        while head.next:
            head = head.next
        return head.val

    def insert(self, index, value):     # insert(index, value) —— 插入值到指定的索引，若索引超出链表长度则报错
        if not self.head:
            raise IndexError("Index out of range")
        head = self.head
        new_node = ListNode(value)
        if index == 0:
            new_node.next = head
            self.head = new_node
            return
        while index - 1 > 0:
            head = head.next
            if not head:
                raise IndexError("Index out of range")
            index -= 1
        temp = head.next
        head.next = new_node
        new_node.next = temp

    def erase(self, index):         # erase(index) —— 删除指定索引的节点，若索引超出链表长度则报错
        if not self.head:
            raise IndexError("Index out of range")
        head = self.head
        if index == 0:
            self.head = head.next
            return
        while index - 1 > 0:
            head = head.next
            if not head:
                raise IndexError("Index out of range")
            index -= 1
        head.next = head.next.next

    def reverse(self):              # reverse() —— 逆序链表 尾插法
        prev = None
        head = self.head
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        self.head = prev

    def remove(self, value):        # remove(value) —— 删除链表中指定值的第一个元素
        if not self.head:
            return
        head = self.head
        if head.val == value:
            self.head = head.next
            return
        while head.next:
            if head.next.val == value:
                head.next = head.next.next
                return
            head = head.next

l1 = LinkedList()
l1.add(1)
l1.add(2)