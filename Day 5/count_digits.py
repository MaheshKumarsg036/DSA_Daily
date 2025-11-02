# https://www.geeksforgeeks.org/problems/count-digits-1606889545/1
class Solution:
    def countDigits(self, n):
    #  code here 
        total = 0
        while n > 0:
            total += 1
            n = n //10
        return total