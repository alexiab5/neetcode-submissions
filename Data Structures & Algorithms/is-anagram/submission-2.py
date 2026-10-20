class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequencies = defaultdict(int)
        
        for i in range(len(s)):
            frequencies[s[i]] += 1
            frequencies[t[i]] -= 1
        
        return all(count == 0 for count in frequencies.values())
