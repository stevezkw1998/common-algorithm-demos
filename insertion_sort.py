nums = [23,2,4,6,2,5,1,6,13,54,8]

def insert_sort(nums):      # 时间复杂度O(n^2)
    if not nums:
        return []
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

print(insert_sort(nums))