class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict()

        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashmap:
                j = hashmap[value]
                return [j, i]
            hashmap[nums[i]] = i
            

