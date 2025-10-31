# https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1

class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        dict_1 = {}
        for c in s:
            dict_1[c] = dict_1.get(c,0) + 1
        sorted_items = sorted(dict_1.items(), key=lambda item: (-item[1], item[0]))
        return sorted_items[0][0]