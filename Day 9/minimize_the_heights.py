# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1

class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        ans = arr[-1] - arr[0]
        min_val = arr[0] + k 
        max_val = arr[-1] - k
        for i in range(len(arr)-1):
            min_local = min(min_val,arr[i+1]-k)
            max_local = max(max_val,arr[i]+k)
            if min_local < 0:
                continue 
            ans = min(ans,max_local-min_local)
        return ans
        
