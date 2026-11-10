class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        current_length = 0
        left = 0
        right = 0
        n = len(s)
        unique = set()

        while right < n:
            if s[right] in unique:
                while s[left] != s[right]:
                    unique.remove(s[left])
                    left += 1
                    current_length -= 1
                
                unique.remove(s[left])
                left += 1
                current_length -= 1
            
            unique.add(s[right])
            right += 1
            current_length += 1
            max_length = max(max_length, current_length)

        return max_length