from .Binary_tree import TreeNode

#find_item(item, root) —— 寻找树中等于某个值的结点, 利用BST的特性, 若一个结点比该值大,
#则往结点的左边寻找, 若一个结点比该值小, 则往结点的右边寻找。时间复杂度为 O(logn)
def find_item(item, root):
    if not root:
        return None
    while root:
        if item == root.val:
            return root
        elif item < root.val:
            root = root.left
        else:
            root = root.right

#find_max(root) —— 寻找树中值最大的结点。由于是BST，最大的结点一定在树的最右边
def find_max(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root

#find_min(root) —— 寻找值最小的结点，一定在树的最左边
def find_min(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root

#add_node(value, root) —— 在二叉搜索树中插入一个新的元素，若元素已存在则忽略
def add_node(value, root):
    if not root:
        return TreeNode(value)
    if value > root.val:
        root.right = add_node(value, root.right)    # 递归插入右子树
    elif value < root.val:
        root.left = add_node(value, root.left)      # 递归插入左子树
    else:
        pass    # 如果value已经存在, 则什么也不做
    return root

#delete_node(value, root) —— 删除一个结点, 分三种情况：
#   1.要删除的是叶结点：直接删除, 将父结点的指针指向None
#   2.要删除的结点只有一个子结点：直接将父结点的指针指向这个子结点
#   3.要删除的结点有左、右两个结点（最复杂的情况）：选取另一结点代替被删结点——右子树的最小元素或左子树的最大元素。
#     可以看到, 右子树的最小元素或左子树的最大元素都是最多只有一个子结点, 因此对它们的删除操作也很简单。
def delete_node(value, root):
    if not root:
        return None     # 说明要删除的元素未找到
    if value < root.val:
        root.left = delete_node(value, root.left)   # 左子树递归删除
    elif value > root.val:
        root.right = delete_node(value, root.right)     # 右子树递归删除
    else:   # 说明已经找到要删除的结点了
        if not root.left:   # 只有右子树或者没有子结点
            return root.right
        elif not root.right:    # 只有左子树
            return root.left
        else:   # 有左右两个节点
            temp = find_min(root.right)     # 在右子树中找到最小的元素
            root.val = temp.val
            root.right = delete_node(temp.val, root.right)
    return root