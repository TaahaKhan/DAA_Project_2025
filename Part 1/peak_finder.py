def find_peak(A, low, high):
    if low == high:
        return low
    
    mid = (low + high) // 2
    
    if A[mid] < A[mid + 1]:
        return find_peak(A, mid + 1, high)
    else:
        return find_peak(A, low, mid)



A = [1, 3, 8, 10, 29, 4, 2]
peak_index = find_peak(A, 0, len(A) - 1)
print("Peak found at index:", peak_index)
print("Peak value:", A[peak_index])