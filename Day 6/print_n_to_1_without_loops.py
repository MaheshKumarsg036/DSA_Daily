# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1

#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        if n == 1:
            print(n,end=" ")
            return
        print(n,end=" ")
        self.printNos(n-1)