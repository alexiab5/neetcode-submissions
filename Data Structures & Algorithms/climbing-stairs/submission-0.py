class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        val1, val2 = 1, 2
        curr = 2
        while curr != n:
            val1, val2 = val2, val1 + val2
            curr += 1
        return val2