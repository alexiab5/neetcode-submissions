class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
            
        max_length = 0
        left = 0
        right = 0
        n = len(s)
        unique = set()

        while right < n:
            if s[right] in unique:
                unique.remove(s[left])
                left += 1
            else:
                unique.add(s[right])
                right += 1
                max_length = max(max_length, right - left)

        return max_length