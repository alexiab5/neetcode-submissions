class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        curr_length = max_length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
            elif nums[i] != nums[i - 1]:
                curr_length = 1
        return max_length
