# Problem1
TALENTRAX TECHNOLOGIES-Backend Developer Screening Assignment

Problem-1

Q1. The gondola takes you up. Strangely, though, the ground doesn't seem to be coming with you; you're not climbing a mountain.
As the circle of Snow Island recedes below you, an entire new landmass suddenly appears above you!.
The gondola carries you to the surface of the new island and lurches into the station.As you exit the gondola, the first thing 
you notice is that the air here is much warmer than it was on Snow Island. It's also quite humid. Is this where the water source is?
The next thing you notice is an Elf sitting on the floor across the station in what seems to be a pile of colourful square cards.
"Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?" You ask about water sources. "I'm not sure; 
I just operate the gondola lift. That does sound like something we'd have, though - this is Island Island, after all! I bet the gardener would know.
 He's on a different island, though - er, the small kind surrounded by water, not the floating kind.
We really need to come up with a better naming scheme. Tell you what: if you can help me with something quick, 
I'll let you borrow my boat and you can go visit the gardener. I got all these scratch cards as a gift, but I can't figure out what I've won."
The Elf leads you over to the pile of colourful cards. There, you discover dozens of scratch cards, all with their opaque covering already scratched off. 
Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. 
You organize the information into a table (your puzzle input).
As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers.
The first match makes the card worth one point and each match after the first doubles the point value of that card.
For example:
Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1
Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). 
Of the numbers you have,Four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points 
(1 for the first match, then doubled three times for each of the three matches after the first).
Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
Card 4 has one winning number (84), so it is worth 1 point.
Card 5 has no winning numbers, so it is worth no points.
Card 6 has no winning numbers, so it is worth no points.
So, in this example, the Elf's pile of scratch cards is worth 13 points.
Take a seat in the large pile of colourful cards. How many points are they worth in Total?

Solution:

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

Explanation:

1.Data Representation:

scratch_cards = [
    (41, 48, 83, 86, 17, [83, 86, 6, 31, 17, 9, 48, 53]),
    (13, 32, 20, 16, 61, [61, 30, 68, 82, 17, 32, 24, 19]),
    (1, 21, 53, 59, 44, [69, 82, 63, 72, 16, 21, 14, 1]),
    (41, 92, 73, 84, 69, [59, 84, 76, 51, 58, 5, 54, 83]),
    (87, 83, 26, 28, 32, [88, 30, 70, 12, 93, 22, 82, 36]),
    (31, 18, 13, 56, 72, [74, 77, 10, 23, 35, 67, 36, 11]),
]

- 'scratch_cards' is a list where each element is a tuple representing a scratch card.
- The first five values in each tuple are the winning numbers, and the last element is a list of numbers we have.

2.Function to Calculate Points:

def calculate_points(winning_numbers, numbers_you_have):
    points = 0
    matches = set(winning_numbers) & set(numbers_you_have)
    
    for match in matches:
        points += 2 ** winning_numbers.index(match)
    
    return points

- The function 'calculate_points' takes two arguments: 'winning_numbers' and 'numbers_you_have'.
- It initializes the variable 'points' to 0 and finds the common numbers ('matches') between the winning numbers 
  and numbers we have using set intersection ('&').
- It then iterates through the common numbers and adds points based on the position of the match in the winning numbers list,
  using the formula '2 ** winning_numbers.index(match)'.
- The calculated points are returned.

3.Calculate Total Points:

total_points = sum(calculate_points(card[:5], card[5]) for card in scratch_cards)

- This line calculates the total points for all scratch cards.
- It uses a list comprehension to iterate through each scratch card in 'scratch_cards'.
- For each scratch card, it calls the 'calculate_points' function with the first five elements as 
  'winning_numbers' and the last element as 'numbers_you_have'.
- The sum function then adds up all the calculated points.

4.Print Result:

print("Total points:", total_points)

- Finally, it prints the total points for all scratch cards.

The code essentially defines a data structure for scratch cards, 
a function to calculate points for a single scratch card, 
and then calculates the total points for all scratch cards.
