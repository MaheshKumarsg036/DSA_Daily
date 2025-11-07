# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0

#User function Template for python3

class Solution:
    def rotate(self, arr):
        arr[0],arr[1:] = arr[-1],arr[:-1]
        return arr