def equivalence_tester(card1, card2):
    return card1 == card2 

def count_equivalent(cards, candidate):
    count = 0
    for card in cards:
        if equivalence_tester(card, candidate):
            count += 1
    return count

def find_majority(cards):
    n = len(cards)
    
    if n == 1:
        return cards[0]
    
    mid = n // 2 
    left_major = find_majority(cards[:mid])
    right_major = find_majority(cards[mid:])
    
    if equivalence_tester(left_major, right_major):
        return left_major
    
    count_left = count_equivalent(cards, left_major)
    count_right = count_equivalent(cards, right_major)
   

    if count_left > n // 2:
        return left_major
    elif count_right > n // 2:
        return right_major
    else:
        return None 


cards = [5, 7, 2, 5, 3, 5, 5, 7, 5, 5]
result = find_majority(cards)

if result is not None:
    print("Yes, there is a majority account:", result)
else:
    print("No majority account found.")