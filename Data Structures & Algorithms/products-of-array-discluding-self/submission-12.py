class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod2 = [nums[n - 1]]
        j = n - 2
        while j >= 0:
            prod2.append(nums[j] * prod2[-1])
            j -= 1
        prod2.reverse()
        res = []
        prod1 = 1
        for i in range(n):
            p2 = prod2[i + 1] if i < n - 1 else 1
            res.append(prod1 * p2)
            prod1 *= nums[i]
        return res