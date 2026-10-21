class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])

        i, j = 0, len(nums) - 1
        while i < j:
            current_sum = sorted_nums[i][0] + sorted_nums[j][0]
            if current_sum == target:
                index1, index2 = sorted_nums[i][1], sorted_nums[j][1]
                if index1 > index2:
                    return [index2, index1]
                else:
                    return [index1, index2]
            elif current_sum < target:
                i += 1
            else:
                j -= 1

        return []

        
            

