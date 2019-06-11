import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

def create_deck():
    deck =[]
    for suit in suits:
        for rank in ranks:
            deck.append(suit +' '+ rank)

    return (deck)

def shuffle_deck(deck):
    random.shuffle(deck)
    return (deck)

deck = create_deck()
print (shuffle_deck(deck))
