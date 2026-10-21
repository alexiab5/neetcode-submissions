class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            frequencies = [0] * 26
            for c in string:
                frequencies[ord(c)- ord('a')] += 1
            
            freqs = tuple(frequencies)
            if freqs in anagrams:
                anagrams[freqs].append(string)
            else:
                anagrams[freqs] = [string]
            
        return list(anagrams.values())
