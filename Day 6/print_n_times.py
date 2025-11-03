# https://www.geeksforgeeks.org/problems/print-gfg-n-times/1&selectedLang=python3
#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return
        print("GFG",end=" ")
        self.printGfg(n-1)