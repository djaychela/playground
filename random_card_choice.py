from random import randint, choice

suits = ['D', 'H', 'C', 'S']
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [suit + card for suit in suits for card in cards]


def shuffle(deck):
    split = randint(10, len(deck))
    deck_1 = deck[:split]
    deck_2 = deck[split:]
    new_deck = []
    for i in range(min(len(deck_1), len(deck_2))):
        new_deck.append(deck_1[i])
        new_deck.append(deck_2[i])
    if len(deck_1) < len(deck_2):
        for i in range(len(deck_1), len(deck_2)):
            new_deck.append(deck_2[i])
    else:
        for i in range(len(deck_2), len(deck_1)):
            new_deck.append(deck_1[i])
    return new_deck


positives = 0
negatives = 0

current_deck = deck
iterations = 100000
for i in range(iterations):
    current_deck = shuffle(current_deck)
    for card in range(len(deck)):
        guess = choice(suits) + choice(cards)
        if guess == current_deck[card]:
            # print(i, card, guess, current_deck[card])
            positives += 1
        else:
            negatives += 1
print(
    f'Success: {positives} from {(iterations * len(deck))} runs, Percentage: {100*(positives / (iterations * len(deck))):2f}%')
