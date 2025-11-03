# https://www.geeksforgeeks.org/problems/sum-of-series2811/1
class Solution:
    def findSum(self, n):
        # code here
        if n == 1:
            return n
        return self.findSum(n-1)+n