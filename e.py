def closest_pair(arr):
    arr.sort()
    return divide(arr)

def divide(arr):
    n = len(arr)
    if n <= 1:
        return float('inf')
    if n == 2:
        return abs(arr[0] - arr[1])
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]
    d1 = divide(left)
    d2 = divide(right)
    d = min(d1, d2)
    return min(d, abs(arr[mid] - arr[mid - 1]))

arr = list(map(float, input().split()))
print(closest_pair(arr))
