class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bkt(nums, k):
            if len(nums) == 0:
                return [[]]

            res = bkt(nums[:k], k - 1)
            n = len(res)
            for i in range(n):
                tmp = res[i].copy()
                tmp.append(nums[k])
                res.append(tmp)
            return res

        return bkt(nums, len(nums) - 1)
            