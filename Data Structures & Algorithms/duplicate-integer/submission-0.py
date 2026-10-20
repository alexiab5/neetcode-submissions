class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencies = collections.defaultdict(int)
        for number in nums:
            frequencies[number] += 1
        
        for number in frequencies:
            if frequencies[number] > 1:
                return True

        return False


        