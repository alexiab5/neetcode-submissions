class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequencies_s = defaultdict(int)
        frequencies_t = defaultdict(int)
        
        for i in range(len(s)):
            frequencies_s[s[i]] += 1
            frequencies_t[t[i]] += 1
        
        return frequencies_s == frequencies_t