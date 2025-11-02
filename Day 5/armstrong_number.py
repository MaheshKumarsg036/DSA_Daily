# https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1

#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        total = 0
        x = n
        while x > 0:
            total += (x%10)**3
            x = x // 10
        return total == n