class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zero = 0

        for num in nums:
            if num:
                product *= num
            else:
                count_zero += 1
        
        res = []
        for i in range(len(nums)):
            if not count_zero:
                res.append(product // nums[i])
            elif count_zero and nums[i] != 0:
                res.append(0)
            else:
                res.append(0 if count_zero > 1 else product)

        return res