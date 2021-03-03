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
                high = mid - 1
            else:
                low = mid + 1