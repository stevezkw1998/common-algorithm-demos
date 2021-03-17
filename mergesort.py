nums = [23,2,4,6,2,5,1,6,13,54,8]

# ------------------归并排序, 时间复杂度最坏情况下O(nlogn)-----------------------
# -----------------------空间复杂度O(n), 临时数组-------------------------------
# ------------------------------稳定排序---------------------------------------
def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return merge(left, right)

def merge(left, right):
    l, r, res = 0, 0, []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    return res + left[l:] + right[r:]

# 优点：
# 1. 时间复杂度最坏O(nlogn), 是基于比较的排序算法所能达到的最高境界
# 2. 是一种稳定排序, 适合链表排序
# 缺点：
# 1. 需要O(n)的空间复杂度, 堆排序空间复杂度O(1), 快排O(logn)

