def find_max_profit(prices, low, high):
    if low == high:
        return 0, prices[low], prices[low]
    
    mid = (low + high) // 2
    
    left_profit, left_min, left_max = find_max_profit(prices, low, mid)
    right_profit, right_min, right_max = find_max_profit(prices, mid + 1, high)
    
    cross_profit = right_max - left_min
    
    best_profit = max(left_profit, right_profit, cross_profit)
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)
    
    return best_profit, overall_min, overall_max



prices = [1, 10, 25, 2, 3, 4]
profit, _, _ = find_max_profit(prices, 0, len(prices) - 1)

if profit > 0:
    print("Maximum profit possible:", profit)
else:
    print("No profit possible.")
