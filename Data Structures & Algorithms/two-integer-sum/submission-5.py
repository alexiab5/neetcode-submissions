class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict()

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hashmap:
                j = hashmap[value]
                if i == j:
                    continue
                elif i < j:
                    return [i, j]
                else:
                    return [j, i]
            

