nums = [23,2,4,6,2,5,1,6,13,54,8]

# ------------------快速排序A, 时间复杂度O(nlogn), 最坏的情况下O(n^2)-----------------------
# ------------------空间复杂度O(logn)-----------------------------------------------------
# ------------------不稳定排序------------------------------------------------------------
def quicksort(nums, left, right):
    if left >= right:
        return
    pivot = left
    i, j = left, right
    while i < j:
        while nums[pivot] <= nums[j] and i < j:
            j -= 1
        while nums[pivot] >= nums[i] and i < j:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[pivot], nums[i] = nums[i], nums[pivot]
    quicksort(nums, left, i-1)
    quicksort(nums, i+1, right)

# ------------------快速排序B, 时间复杂度O(nlogn), 最坏的情况下O(n^2)-----------------------
def quicksort2(nums, left, right):          # 用栈代替递归
    if left >= right:
        return
    stack = []
    while stack or left < right:
        if left < right:
            pivot = left
            i, j = left, right
            while i < j:
                while nums[pivot] <= nums[j] and i < j:
                    j -= 1
                while nums[pivot] >= nums[i] and i < j:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[i] = nums[i], nums[pivot]
            stack.append((left, i, right))
            right = i - 1
        else:
            left, mid, right = stack.pop()
            left = mid + 1

quicksort2(nums, 0, len(nums)-1)
print(nums) 

# ------------------------快速排序的优化----------------------------
# ------------------------A三数中值快速排序-----------------------------
def quicksort_opt1(nums, left, right): 
    if left >= right:
        return
    stack = []
    while stack or left < right:
        if left < right:
            l, m, r = left, (right-left)//2, right # 第一个, 中间位置, 最后一个
            pivot = findmedian(l, m, r) # 三数取中值法选取枢轴元pivot
            i, j = left, right
            while i < j:
                while nums[pivot] <= nums[j] and i < j:
                    j -= 1
                while nums[pivot] >= nums[i] and i < j:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            nums[pivot], nums[i] = nums[i], nums[pivot]
            stack.append((left, i, right))
            right = i - 1
        else:
            left, mid, right = stack.pop()
            left = mid + 1

def findmedian(l, m, r):
    if nums[l] <= nums[m]:
        if nums[m] <= nums[r]:
            return m
        else:
            if nums[l] >= nums[r]:
                return l
            else:
                return r
    else:
        if nums[m] >= nums[r]:
            return m
        else:
            if nums[l] >= nums[r]:
                return r
            else:
                return l

# ------------------------快速排序重复元素处理-----------------------------
# ------------------------B双路快速排序-----------------------------------
def quicksort_opt2(nums, left, right): 
    if left >= right:
        return
    stack = []
    while stack or left < right:
        if left < right:
            l, m, r = left, (right-left)//2, right # 第一个, 中间位置, 最后一个
            pivot = findmedian(l, m, r) # 三数取中值法选取枢轴元pivot
            nums[pivot], nums[left] = nums[left], nums[pivot]
            pivot = left
            i, j = left+1, right
            while i <= j:   # 为什么不能是 i < j?
                # 此处先平移j和先平移i对结果没有影响
                while nums[i] < nums[pivot] and i <= j:
                    #不能改为nums[i] <= nums[pivot], 因为这种方式将连续出现的这些值归为其中一方, 使得两棵树不平衡
                    i += 1
                while nums[j] > nums[pivot] and i <= j: 
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    i += 1
            nums[pivot], nums[j] = nums[j], nums[pivot] 
            #因为pivot放置在左边, 所以不可与左侧指针i交换---->会造成无限循环
            stack.append((left, j, right))  
            right = j - 1
        else:
            left, mid, right = stack.pop()
            left = mid + 1

nums = [23,2,4,6,2,5,1,6,13,54,8]
quicksort_opt2(nums, 0, len(nums)-1)
print(nums) 