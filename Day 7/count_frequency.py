# https://www.geeksforgeeks.org/dsa/counting-frequencies-of-array-elements/
def countFreq(arr):

    freq = {}

    ans = []


    for num in arr:
        freq[num] = freq.get(num, 0) + 1


    for num, freq in freq.items():
        ans.append([num, freq])

    return ans

