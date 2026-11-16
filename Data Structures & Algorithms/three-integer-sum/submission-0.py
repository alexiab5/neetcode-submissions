class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)
        nums.sort()
        frequencies = {}

        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        for i in range(n):
            for j in range(i + 1, n):
                frequencies[nums[i]] -= 1
                frequencies[nums[j]] -= 1
                val3 = -nums[i] - nums[j]
                if val3 in frequencies and frequencies[val3] > 0:
                    x = None
                    if val3 <= nums[i]:
                        x = (val3, nums[i], nums[j])
                    elif val3 >= nums[j]:
                        x = (nums[i], nums[j], val3)
                    else:
                        x = (nums[i], val3, nums[j])
                    if x not in result:
                        result.add(x)
                frequencies[nums[i]] += 1
                frequencies[nums[j]] += 1
        
        return [list(x) for x in result]
