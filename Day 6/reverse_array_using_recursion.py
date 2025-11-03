# https://www.geeksforgeeks.org/problems/reverse-an-array/1

class Solution:
    def reverseArray(self, arr,start=0):
        # code here
        n = len(arr)
        if start == n//2:
            return arr
        arr[start],arr[n-start-1] = arr[n-start-1],arr[start]
        start += 1
        self.reverseArray(arr,start)
        return arr
        
        
        