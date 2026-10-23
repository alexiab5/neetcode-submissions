class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        top = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[0:k]
        res = []
        for num, freq in top:
            res.append(num)
        return res
        