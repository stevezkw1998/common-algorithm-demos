'''
堆（Heap）/二叉堆（Binary Heap）:用数组表示的完全二叉树。性质：从根到任一结点的路径是有序的。
    最大堆（MaxHeap）：也叫大顶堆，任一结点的值是其子树所有结点的最大值（大于等于）;
    最小堆（MinHeap）：也叫小顶堆，任一结点的值是其子树所有结点的最小值（小于等于）;

堆最主要的两个操作是插入和删除，以最大堆为例:
    插入：先判断堆是否已满。新插入的结点放在完全二叉树最后的位置，然后和父结点比较，如果比父结点大，
        则交换两者位置，继续向上比较，直到不比父结点大或成为根结点。时间复杂度是树的高度 O(log n)
    删除：删除操作指的是删除根结点。先判空，用完全二叉树中的最后一个结点代替根节点，然后不断和子结点比较，
        和较大的那个子结点交换位置。时间复杂度 O(log n)

堆的建立：从一个序列中建立一个堆，如果每个元素分别插入，时间复杂度是O(nlog n)，因此选取另一种方法，
        先将序列放入数组，再从倒数第二层开始，从左到右/从右到左依次向下调整为堆，直到调整到树根，时间复杂度为 O(n)

和二叉搜索树相比，堆的内存占用更小（使用数组实现）；BST必须平衡的情况下才能达到 O(log n) 的复杂度，但是堆的复杂度始终是 O(log n)；
对于搜索元素，BST更快，堆不是用来搜索元素的，堆的主要操作是快速插入、删除元素，在堆中搜索元素等同于在数组中搜索元素

那优先队列有什么用呢？为什么不直接把元素排序然后再将这个有序数组作为优先队列呢？一个原因是在某些应用中，总数据量太大，无法进行排序，
比如一个10亿规模的数据，而我们只想从中找出最大的10个数，有了优先队列，我们只需要一个存储10个数的队列即可

既然使用数组实现，那就不像二叉树那样有指向子结点的指针，所以在堆中如何进行定位呢？实现堆时，规定下标从1开始，那么对于一个下标为i的结点，有：
parent = i // 2
c1 = 2 * i
c2 = 2 * i + 1
'''
class Heap:
    def __init__(self):
        self.data = [None]  # 如果是0, 1, 2的话, 2 // 2 = 1得不到parent, 所以采用1, 2, 3

# 实现一个最大堆
class MaxHeap(Heap):
    def __init__(self):
        super(MaxHeap, self).__init__() 

    def is_empty(self):     # is_empty() —— 判断堆是否为空
        return self.get_size == 0

    def get_size(self):     # get_size() —— 获取堆中的元素个数
        return len(self.data)-1

    def peek_max(self):     # peek_max() —— 返回堆顶元素，但不删除
        return self.data[1]

    def insert(self, value):    # insert(value) —— 向堆中插入元素
        self.data.append(value)
        index = self.get_size()
        # 如果比父结点大并且不是根结点则向上调整
        while index > 1 and self.data[index] > self.data[index//2]:
            self.data[index], self.data[index//2] = self.data[index//2], self.data[index]
            index = index // 2

    def sift_down(self, index): # 用于删除和创建堆的函数。从当前结点开始向下调整，保证结点往下是一个堆
        while 2 * index <= self.get_size():
            # 左子节点的索引
            child = 2 * index
            # 如果右子结点存在且比左子结点大，则应与右子结点交换
            if 2 * index + 1 <= self.get_size() and self.data[2*index+1] > self.data[child]:
                child += 1 # 右子节点的索引
            # 如果当前结点的值小于子结点中的较大者，则应继续向下交换，否则结束
            if self.data[index] < self.data[child]:
                self.data[index], self.data[child] = self.data[child], self.data[index]
                index = child
            else:
                break

    def remove(self):       # remove() —— 删除堆顶元素(最大值)
        if self.is_empty():
            raise RemoveError("Unable to remove from an empty heap.")
        # 用堆的最后一个元素替代顶堆元素, 然后删除最后一个元素
        self.data[1], self.data[self.get_size()] = self.data[self.get_size()], self.data[1]
        self.data.pop()
        # 从堆顶向下调整
        self.sift_down(1)

    def build_heap(self, array):    # build_heap(array) —— 从一个序列创建堆
        self.data = [None] + array
        index = self.get_size() // 2
        # 从倒数第二层开始, 从右到左, 逐层向上调整。每次调整只需sift_down
        while index > 0:
            self.sift_down(index)
            index -= 1