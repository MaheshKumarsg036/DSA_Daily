# https://www.geeksforgeeks.org/problems/prime-number2314/1
class Solution:
    def isPrime(self, n):
        # code here
        if n == 1:
            return False
        if n == 2:
            return True
        i = 2
        while i *i <=n:
            if n % i ==0:
                return False
            i += 1
        return True