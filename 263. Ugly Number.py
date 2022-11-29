class Solution:
    def isUgly(self, n: int) -> bool:
        #if n == 1 or (n % 2 ==0 and n % 3 == 0) or (n % 2 ==0 and n % 5 == 0) or (n % 5 ==0 and n % 3 == 0):
            #return True
       #else: 
            #return False
        k = 1
        while n // k < n:
            if (n == 1):
                return True
            n = n % k
            print(k)
            k += 1
            if (k != 2 or k != 3 or k!= 5 ):
                return False
            else: 
                return True
                
s = Solution()
asd = s.isUgly(6)
print(asd)

