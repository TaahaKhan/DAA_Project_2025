import math

def findMedian(A, B, n, a=0, b=0):
    
    if n == 1:
        return min(A[a], B[b])
    
    k = math.ceil(n / 2)

    if A[a + k - 1] < B[b + k - 1]:
        return findMedian(A, B, k, a + math.floor(n / 2), b)
    else:
        return findMedian(A, B, k, a, b + math.floor(n / 2))


A = [2, 4, 6, 8, 10, 14, 16, 18, 20, 22]
B = [4, 5, 10, 13, 14, 17, 21, 22, 29, 30]
n = len(A)

median_value = findMedian(A, B, n)
print("Median of combined data:", median_value)