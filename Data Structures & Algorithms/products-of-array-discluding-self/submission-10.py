class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        [1 2 8 48]
        [48 48 24 6]
        """
        n = len(nums)
        prod1 = [nums[0]]
        prod2 = [nums[n - 1]]
        i, j = 1, n - 2
        while i < n and j >= 0:
            prod1.append(nums[i] * prod1[i - 1])
            prod2.append(nums[j] * prod2[i - 1])
            i += 1
            j -= 1
        prod2.reverse()
        res = []
        for i in range(n):
            p1 = prod1[i - 1] if i > 0 else 1
            p2 = prod2[i + 1] if i < n - 1 else 1
            res.append(p1 * p2)
        return res