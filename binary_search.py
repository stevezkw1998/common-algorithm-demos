class Solution:
    def binarysearch(self, nums, target):
        #   循环实现    时间复杂度O(logn)
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    # 如果nums=[1,2,7,7,7,7,7,9], target=7, 查找最左侧的7怎么办?
    def binarysearch2(self, nums, target):  # 时间复杂度O(logn)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid-1] != target:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
nums=[1,2,7,7,7,7,7,9]
s = Solution()
ans = s.binarysearch2(nums, 7)
print(ans)