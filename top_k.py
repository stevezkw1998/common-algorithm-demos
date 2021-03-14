nums = [23,1,3,4,3,6,21,15,64,8]
k = 4

def solution(nums, k):
    ans = quickselect(nums, k, 0, len(nums)-1)
    ans2 = heapsort(nums, k)
    print(ans)
    print(ans2)

# ------------------快速排序, 时间复杂度O(nlogn)------------------------
# -------------最坏情况下(nums本来就有序), 时间复杂度O(n^2)--------------
def quickselect(nums, k, left, right):
    if left == right:
        return nums[right]
    index = partition(nums, left, right)
    if right - index + 1 == k:
        return nums[index]
    elif right - index + 1 > k:
        return quickselect(nums[:], k, index+1, right)
    else:
        return quickselect(nums[:], k-right+index-1, left, index-1)

def partition(nums, left, right):
    if left == right:
        return right
    i, j = left, right
    while i < j:
        while nums[left] <= nums[j] and i < j:
            j -= 1
        while nums[left] >= nums[i] and i < j:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[j] = nums[j], nums[left]
    return j

# ------------------堆排序, 时间复杂度 <= O(nlogk)-------------------------
# ---------最坏情况下(每次都要全堆heapify), 时间复杂度O(nlogk)--------------
def heapsort(nums, k):
    #  先将前k个数变成小顶堆
    nums = heapinsert(nums, k)
    for i in range(k, len(nums)):
        if nums[i] > nums[0]:
            nums[0] = nums[i]
            nums = heapinsert(nums, k)
    return nums[0]

def heapinsert(nums, k):
    #  将列表变为小顶堆
    for index in range(1, k):
        while nums[(index-1) // 2] > nums[index] and index > 0:
            nums[(index-1) // 2], nums[index] = nums[index], nums[(index-1) // 2]
            index = (index-1) // 2
    return nums 

    
solution(nums, k)