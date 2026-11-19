class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr_permutation = []
        n = len(nums)
        used = [False] * n

        def bkt(k):
            if k == n:
                result.append(curr_permutation.copy())
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr_permutation.append(nums[i])
                    bkt(k + 1)
                    curr_permutation.pop()
                    used[i] = False
        
        bkt(0)
        return result
    