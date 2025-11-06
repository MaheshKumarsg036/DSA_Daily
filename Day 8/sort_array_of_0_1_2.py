#https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0

class Solution:
    def sort012(self, arr):
        # code here
        zeros,ones,twos = 0,0,0
        for i in arr:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1
        
        j = 0
        for i in range(zeros):
            arr[j] = 0
            j += 1
        for i in range(ones):
            arr[j] = 1
            j += 1
        for i in range(twos):
            arr[j] = 2
            j += 1
        return arr