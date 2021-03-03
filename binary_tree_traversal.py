class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preordertraversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def preorder(self, root):   # 用栈来代替递归
        if not root:
            return []
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.val)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return res

    def levelordertraversal(self, root):
        from collections import deque   # 层序遍历(广度优先遍历)基本上是由deque队列实现的
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res

    def levelorder(self, root):    # 时间复杂度O(n), 空间复杂度O(n)
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            root = queue.pop(0)
            res.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return res

    # 二叉树的后序遍历, 非递归版本: 非递归的后序遍历是 hard 难度, 所以专门在这里写一下。有下面几种思路:

    #   前序遍历是“根-左-右”, 稍微改一下, 就可以变成“根-右-左”,
    #   而将最后的结果倒序输出, 就是后序遍历“左-右-根”的顺序了。时间复杂度依然为 O(n):
    def postorder_1(root):
        if not root:
            return []
        res = []
        stack = []
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root.val)
                root = root.right
            else:
                root = stack.pop()
                root = root.left
        # res1 用来存放 res 的倒序输出, 也可以直接使用 res[::-1]
        res1 = []
        for i in range(len(res)):
            res1.append(res.pop())
        return res1

    #   使用两个栈实现, 这个思路也比较易于理解。后序遍历是“左-右-根”, 
    #   所以对于一个栈来说，应该先push根结点，然后push右结点，最后push左结点:
    def postorder_2(root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        # 此时res中存放了倒序的结点, 使用res1将其倒序输出并取结点的值
        res1 = []
        for i in range(len(res)):
            res1.append(res.pop().val)
        return res1