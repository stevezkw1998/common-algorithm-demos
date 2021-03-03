nums = [23,2,4,6,2,5,1,6,13,54,8]

def select_sort(nums):      # 时间复杂度O(n^2)
    if not nums:
        return []
    for i in range(len(nums)-1):
        smallest = i
        for j in range(i, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
            nums[i], nums[smallest] = nums[smallest], nums[i]
    return nums

print(select_sort(nums))