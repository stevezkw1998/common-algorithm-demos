#   思路：hash表存储键=链表中节点的值, 值指向节点的位置; 链表存储cache中的数据
#   时间复杂度O(1), 空间复杂度O(1)

#   -----------------------------------方法A------------------------------------
#   用一种Python自带的结合了哈希表与双向链表的数据结构 OrderedDict, 类似Java中的 LinkedHashMap
from collections import OrderedDict
class LRUcacheA(OrderedDict):
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)   # 更新键值到最近使用
        return self[key]
    
    def put(self, key, value):
        if key in self:
            self.move_to_end(key)   # 更新键值到最近使用
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)    #  如果超出长度, 就把上一次被使用距离最久的删除

#   -----------------------------------方法B------------------------------------
# 哈希表 + 双向链表
# 用一个哈希表和一个双向链表维护所有在缓存中的键值对：
#     1.双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
#     2.哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
#   时间复杂度O(1), 空间复杂度O(capacity) = O(1)
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUcacheB:
    def __init__(self, capacity):
        self.cache = dict() #  维护一个hashmap 存放 key:node
        # 使用伪头部和伪尾部节点
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        # 如果 key 存在, 先通过hashmap定位, 再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            # 如果 key 不存在, 创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进hashmap
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量, 删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在, 先通过 hashmap 定位, 再修改 value, 并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node