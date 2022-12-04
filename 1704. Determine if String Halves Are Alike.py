class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        slovar = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        count_1, count_2 = 0, 0
        for i in range(len(s)//2):
            if s[i] in slovar:
                count_1 += 1
        for i in range(len(s)//2, len(s)):
            if s[i] in slovar:
                count_2 += 1
        if count_1 == count_2:
            return True
        else:
            return False