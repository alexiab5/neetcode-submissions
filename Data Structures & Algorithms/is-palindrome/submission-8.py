class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = ''
        for char in s:
            if char.isalpha():
                if char.isupper():
                    char = char.lower()
                copy += char
            if char.isdigit():
                copy += char
                
        i, j = 0, len((copy)) - 1
        while i <= j:
            if copy[i] != copy[j]:
                return False
            i += 1
            j -= 1
        
        return True