import random

def get_numbers_ticket(min_val, max_val, quantity):
    
    if (min_val < 1 or 
        max_val > 1000 or 
        quantity < 1 or 
        quantity > (max_val - min_val + 1) or 
        min_val > max_val):
        return []

    try:
        numbers_range = range(min_val, max_val + 1)
        lottery_numbers = random.sample(numbers_range, k=quantity)
        lottery_numbers.sort()
        
        return lottery_numbers
        
    except (ValueError, TypeError):
        return []

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)