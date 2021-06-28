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
# ------------------------A三路快速排序-----------------------------
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

