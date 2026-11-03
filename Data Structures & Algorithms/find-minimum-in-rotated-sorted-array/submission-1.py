class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[n - 1]:
            return nums[0]
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if nums[m] < nums[0]:
                r = m
            else:
                l = m