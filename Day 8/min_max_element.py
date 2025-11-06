# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

class Solution:
    def getMinMax(self, arr):
        # code here
        max_ele,min_ele = arr[0],arr[0]
        
        for i in arr[1:]:
            if i < min_ele:
                min_ele = i
            if i > max_ele:
                max_ele = i
        return [min_ele,max_ele]