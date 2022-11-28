class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = "abba"
        s = "dog cat cat dog"
        slovar = dict()
        for i in range(len(pattern)):
        for j in range(len(s)):
            if s[i] == ' ':

