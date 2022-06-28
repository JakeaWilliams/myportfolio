# %% [markdown]
# # Blackjack 
# ## Gameplay
# <b>
# To play a hand of Blackjack the following steps must be followed: </b> <br>
# 1. Shuffle the deck <br>
# 2. Deal two cards to each player <br>
# 3. Show the cards <br>
# 4. Ask the player if he wants to hit or stay <br>
# 5. If the player chooses to hit, he must draw a card and show the cards <br>
# 6. If the player chooses to stay, the dealer must draw a card and show the cards <br>
# 7. Compare the cards and determine the winner <br>
# 8. If the player wins, he must pay the dealer <br>
# 9. If the dealer wins, he must pay the player <br>
# 10. If the player and the dealer tie, the player and dealer must pay each other <br>
# 11. The game ends when the player or the dealer has gone over 21 <br>
# 12. Ask the player if he wants to play again <br>
# 13. If the player chooses to play again, the game must be restarted <br>
# 14. If the player chooses to quit, the game must end <br>
# </b>
# 

# %% [markdown]
# # Playing Cards
#  A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting. As a starting point in your program, you may want to assign variables to store a list of suits, ranks, and then use a dictionary to map ranks to values.

# %%
# start by importing a random module
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

# %%
# CARD CLASS
# a card only has a suit and a rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
# Return the card's rank in string format
    def __str__(self):
        return self.rank + ' of ' + self.suit

# %%
# DECK CLASS
# iterate over sequences of suits and ranks

# create a deck of cards
class Deck:
    # initialize a deck of cards
    def __init__(self):
        self.deck = [] # start with an empty list
        # iterate over the suits
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    # return the number of cards in the deck
    def __str__(self):
        deck_comp = ''
        # iterate over the deck
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        # return the deck of cards
        return 'The deck has:' + deck_comp
    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)
    # deal a card from the deck
    def deal(self):
        single_card = self.deck.pop()
        # return the card
        return single_card


# %%
#test to see if the deck is working
test_deck = Deck()
print(test_deck)

# %%
# HAND CLASS
class Hand:
    # start with an empty list
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    # add a card to the hand
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    # if the value of the hand is greater than 21 and there is an ace,
    # then adjust for the ace
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# %%
#add two cards to the hand and test if the value obtained is correct
test_hand = Hand()
test_deck = Deck()
test_deck.shuffle()
test_hand.add_card(test_deck.deal())
test_hand.add_card(test_deck.deal())
test_hand.adjust_for_ace()

# %%
# test_hand.__str__()
for card in test_hand.cards:
    print(card)

# %%
#Ace is 11 by default, but if the total value is more than 21, then it is 1
class Hand:
    #create a hand object
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    #add card to the hand
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    #adjust for ace
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    

# %%
#CREATE CHIPS CLASS
class Chips:
    #setting up the chips
    def __init__(self):
    #player starts with 100 chips
        self.total = 100
    #function to bet
        self.bet = 0
    #function to win the bet
    def win_bet(self):
        self.total += self.bet
    #function to lose the bet
    def lose_bet(self):
        #if the total is less than the bet, then the total is 0
        self.total -= self.bet


# %%
# take a bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an whole number!')
        else:
            if chips.bet > chips.total:
                print("Sorry, you'd bust with that bet. You have",chips.total,"chips left.")
            else:
                break

# %%
# player chose hit 
def hit(deck,hand):
    # add a card to the hand
    hand.add_card(deck.deal())
    # adjust for ace
    hand.adjust_for_ace()
    


# %%
# dealer asks if the player wants to hit or stand
def hit_or_stand(deck,hand):
    global playing # to control an upcoming while loop
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break

# %%
#display cards, show the value of the hand
def show_some(player,dealer):
    # show some cards, hide one
    print("\nDealer's Hand:")
    # print the first card of the dealer's hand
    print(" <card hidden>")
    # print the second card of the dealer's hand
    print('',dealer.cards[1])  # print second card
    # print the player's hand
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    # print the value of the player's hand
    print("\nPlayer's Hand =", player.value)
    # print the value of the dealer's hand
    print("\nDealer's Hand =", dealer.value)


# %%
# end of game scenario 
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

# player and dealer tie
def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

# dealer busts - player wins
def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
# dealer wins - player loses
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
# push - no one wins 
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


# %%
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    #Player's Hand
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    #Dealer's Hand
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            # dealer busts
            dealer_busts(player_hand,dealer_hand,player_chips)
        #dealer wins
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        #player wins
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        #push
        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total after the game
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    # If Player enters 'y', player starts a new game
    if new_game[0].lower()=='y':
        playing=True
        continue
    # If Player enters 'n', player quits the game
    else:
        print("Thanks for playing!")
        #exit()
        break

            


