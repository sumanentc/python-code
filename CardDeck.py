import random;

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True;


# CLASS DEFINTIONS:

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

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
        # Card passed in
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        # Check my card value greater than 21 and adjust my ace value to 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips():
    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total +=self.bet

    def lose_bet(self):
        self.total -=self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How may chips would you like to bet? "))
        except ValueError:
            print("Value must be an Integer")
        else:
            if(chips.bet> chips.total):
                print("Sorry, your bet cannot exceed ", chips.total)
            else:
                break;
def hit(deck,hand):
    single_card = deck.deal();
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s ")

        if(x[0].lower()=='h'):
            hit(deck,hand)

        elif(x[0].lower()=='s'):
            print("Player Stand Dealer's Turn ")
            playing=False;
        else:
            print("Sorry I didn't understand that , Please Enter h or s only ! ")
            continue
        break;

def player_busts(player,dealer,chips):
    print("Bust Player !! ")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins !! ")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Player Wins Dealer Busted !! ")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer Wins !! ")
    chips.win_bet()

def push(player, dealer):
    print("Dealer And Player Tie !! ")



while True:
    print("Welcome to BlackJack !!!")

    deck = Deck();
    deck.shuffle()

    player_hand = Hand();
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand();
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    while playing:
        hit_or_stand(deck,player_hand)

        if(player_hand.value > 21):
            player_busts(player_hand,dealer_hand,player_chips)
            break;

        if(player_hand.value<=21):

            while(dealer_hand.value<player_hand.value):
                hit(deck,dealer_hand)

            if(dealer_hand.value > 21):
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif(dealer_hand.value > player_hand.value):
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif(dealer_hand.value < player_hand.value):
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)

    new_game = input("Would you like to Play Another Hand ? y/n : ")

    if(new_game[0].lower()=='y'):
        playing=True
        continue

    else:
        print("Thank for Playing !!!")
        break;




