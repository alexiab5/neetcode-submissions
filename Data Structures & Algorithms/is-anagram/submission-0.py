class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencies_s = defaultdict(int)
        frequencies_t = defaultdict(int)
        
        for i in range(ord('a'), ord('z') + 1):
            frequencies_s[chr(i)] = frequencies_t[chr(i)] = 0
        
        for letter in s:
            frequencies_s[letter] += 1
        
        for letter in t:
            frequencies_t[letter] += 1
        
        for letter in frequencies_s.keys():
            if frequencies_s[letter] != frequencies_t[letter]:
                return False
        
        return True