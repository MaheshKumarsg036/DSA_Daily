# https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        curr_max,max_sum = arr[0],arr[0]
        
        for i in range(1,len(arr)):
            curr_max = max(arr[i],curr_max+arr[i])
            max_sum = max(max_sum,curr_max)
        return max_sum
            