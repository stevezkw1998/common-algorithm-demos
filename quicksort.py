nums = [23,2,4,6,2,5,1,6,13,54,8]

# ------------------快速排序, 时间复杂度O(nlogn)-----------------------
def quicksort(nums, left, right):
    if left >= right:
        return
    i, j = left, right
    while i < j:
        while nums[left] <= nums[j] and i < j:
            j -= 1
        while nums[left] >= nums[i] and i < j:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[i] = nums[i], nums[left]
    quicksort(nums, left, i-1)
    quicksort(nums, i+1, right)

quicksort(nums, 0, len(nums)-1)
print(nums) 