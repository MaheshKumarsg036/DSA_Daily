#https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1

class Solution:
    def gcd(self, a, b):
        # code here
        if a == 0:
            return b
        return self.gcd(b%a,a)