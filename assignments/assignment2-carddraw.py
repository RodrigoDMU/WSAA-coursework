# ----------------------------------------------------------------------------------------------------------------------------------------
# Assignment: Deal cards
# ----------------------------------------------------------------------------------------------------------------------------------------
# - Look at the the page Deck of Cards API. This is an API that simulates dealing a deck of cards.
# - Write a program that "deals" (prints out) 5 cards, first you need to shuffle, get the deck_id, with the deck_id you can get the cards.
# - This example gets two cards. From there you need to print the value and the suit of each card and save the file as 
# assignment2-carddraw.py (or as a notebook)
# - Last few marks: Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.
# ----------------------------------------------------------------------------------------------------------------------------------------
# Author: Rodrigo De Martino Ucedo
# ----------------------------------------------------------------------------------------------------------------------------------------

# It allows you to send HTTP requests using Python.
import requests

# Shuffle the deck.
shuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(shuffle_url)
deck_id = response.json()['deck_id']

# Draw 5 cards.
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(draw_url)
cards = response.json()['cards']

# Print the value and suit of each card.
print("You have drawn the following cards:")
drawn_cards = []
for card in cards:
    print(f"{card['value']} of {card['suit']}")
    drawn_cards.append((card['value'], card['suit']))

# Check for pairs, triples, straights, or all same suit.
values = [card[0] for card in drawn_cards]
suits = [card[1] for card in drawn_cards]

# Check for pairs, triples, etc.
from collections import Counter

value_counts = Counter(values)
suit_counts = Counter(suits)

# Checking for pairs or triples.
pairs = [value for value, count in value_counts.items() if count == 2]
triples = [value for value, count in value_counts.items() if count == 3]

# Checking for straight (sequence of values).
value_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING", "ACE"]
sorted_values = sorted([value_order.index(value) for value in values])
straight = sorted_values == list(range(min(sorted_values), min(sorted_values) + 5))

# Checking for all same suit.
same_suit = len(suit_counts) == 1

# Step 5: Congratulate the user if a pattern is found.
if len(pairs) > 0:
    print(f"\nYou have a pair of {', '.join(pairs)}!")
elif len(triples) > 0:
    print(f"\nYou have a triple of {', '.join(triples)}!")
elif straight:
    print("\nYou have a straight!")
elif same_suit:
    print("\nYou have drawn all cards from the same suit!")

# If no special pattern, let the user know.
if not (len(pairs) > 0 or len(triples) > 0 or straight or same_suit):
    print("\nNo special patterns found.")

# END