class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencies: dict[int, int] = {}
        for number in nums:
            if frequencies.get(number) is None:
                frequencies[number] = 1
            else:
                frequencies[number] += 1
        
        for number in frequencies:
            if frequencies[number] > 1:
                return True

        return False


        