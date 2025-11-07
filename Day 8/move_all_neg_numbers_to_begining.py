def move(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while right > left and arr[left] < 0:
            left += 1
        while right > left and arr[right] > 0:
            right -= 1
        if right > left:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr