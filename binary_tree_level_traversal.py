class Solution:
    def leveltraversal(self, root):
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