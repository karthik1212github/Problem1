scratch_cards = [
    (41, 48, 83, 86, 17, [83, 86, 6, 31, 17, 9, 48, 53]),
    (13, 32, 20, 16, 61, [61, 30, 68, 82, 17, 32, 24, 19]),
    (1, 21, 53, 59, 44, [69, 82, 63, 72, 16, 21, 14, 1]),
    (41, 92, 73, 84, 69, [59, 84, 76, 51, 58, 5, 54, 83]),
    (87, 83, 26, 28, 32, [88, 30, 70, 12, 93, 22, 82, 36]),
    (31, 18, 13, 56, 72, [74, 77, 10, 23, 35, 67, 36, 11]),
]

# Function to calculate points for a single scratch card
def calculate_points(winning_numbers, numbers_you_have):
    points = 0
    matches = set(winning_numbers) & set(numbers_you_have)
    
    for match in matches:
        points += 2 ** winning_numbers.index(match)
    
    return points

# Calculate total points for all scratch cards
total_points = sum(calculate_points(card[:5], card[5]) for card in scratch_cards)

print("Total points:", total_points)