import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'



class Deck:
    def __init__(self,):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += card.__str__() + '\n'

        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # Card passed in from Deck.deal() --> singleCard(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # Track Aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        # IF VALUE > 21 AND I STILL HAVE AN ACE
        # THAN CHANGE MY ACE TO BE A 1 INSTEAD OF 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter the amount for bet: "))
        except:
            print('Whoops! You did not enter the correct value!! Please provide an Integer.')
            continue
        else:
            if chips.bet > chips.total:
                print("Sorry! You don't have enough chips.You have {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s: ')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stand Dealer's turn.")
            playing = False
        else:
            print("I do not understand. Please enter h or s only.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player,dealer,chips):
    print('Player Bust! Dealer Wins!')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print('Player Wins!')
    chips.win_bet()


def dealer_busts(player,dealer,chips):
    print('Player Wins! Dealer Bust')
    chips.lose_bet()


def dealer_wins(player,dealer,chips):
    print('Dealer Wins!')
    chips.lose_bet()


def push():
    print("Dealer and Player tie! BUST")


while True:
    # Print an opening statement
    print("Welcome To BLACKJACK!!")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)

        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,player_chips)

            break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:

        while dealer.value < 17:
            hit(deck,dealer)

        # Show all cards
        show_all(player, dealer)

            # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)

        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)

        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)

        else:
            push()

        # Inform Player of their chips total
    print("You have {} chips left.".format(player_chips.total))

        # Ask to play again
    new_game = input("Want to play again! Y/N")
    if new_game[0].upper() == 'Y':
        playing = True
        continue
    else:
        print('Thank You!')
        break

