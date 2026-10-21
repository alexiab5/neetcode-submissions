class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = [(nums[i], i) for i in range(len(nums))]
        values = sorted(values)
        
        for i in range(len(values)):
            start = i + 1
            end = len(values) - 1
            other = target - values[i][0]
            while start <= end:
                mid = (start + end) // 2
                if values[mid][0] == other:
                    index1 = values[i][1]
                    index2 = values[mid][1]
                    if index1 > index2:
                        return [index2, index1]
                    else:
                        return [index1, index2]
                elif values[mid][0] > other:
                    end = mid - 1
                else:
                    start = mid + 1
