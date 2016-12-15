# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank
            
    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object

    def __str__(self):
        answer = "Hand contains "
        for elt in self.hand:
            answer += str(elt) + " "
        # return a string representation of a hand
        return answer
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        number_of_aces = 0
        for card in self.hand:
            if card.rank == 'A':
                number_of_aces += 1
        value = 0
        for card in self.hand:
            value += VALUES[card.rank]
            
        for i in range(number_of_aces):
            if value + 10 < 21:
                value += 10
        return value 
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        offset = 0
        for card in self.hand:
            
            card.draw(canvas, [offset * CARD_SIZE[1]/1.3\
                               + pos[0],
                               pos[1]])
            offset += 1
# define deck class 
class Deck:
    def __init__(self):
        
        self.deck = [Card(suit, rank)\
                          for suit in SUITS\
                          for rank in RANKS]        
        
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        # return a string representing the deck
        answer = "Hand contains "
        for elt in self.hand:
            answer += str(elt) + " "
        # return a string representation of a hand
        return answer


#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global deck
    global player, dealer
    if in_play:
        score -= 1
    
    deck = Deck()
    deck.shuffle()
    
    player = Hand()
    dealer = Hand()
    
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())  
    
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = "Hit or Stand ?"
    in_play = True

def hit():
    # replace with your code below
    global outcome, in_play, score
    # if the hand is in play, hit the player
    if not in_play:
        return
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        outcome = "you have busted"
        score -= 1
        in_play = False
        
def stand():
    # replace with your code below
    global in_play, outcome, score
    
    if not in_play:
        return
    
    if player.get_value() > 21:
        return
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer.get_value() < 18:
        dealer.add_card(deck.deal_card())
    
    # assign a message to outcome, update in_play and score
    if dealer.get_value() > 21:
        outcome = "you win, dealer busted !"
        score += 1
        in_play = False
        return
    else:
        if player.get_value() <= dealer.get_value():
            outcome = "dealer win !"
            score -= 1
            in_play = False
        else:
            outcome = "player win !"
            score += 1
            in_play = False
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BlackJack", (200, 50), 40, "white")
    canvas.draw_text(outcome, (200, 150), 32, "white")
    canvas.draw_text("New deal ?", (200, 100), 32, "white")
    
    
    canvas.draw_text("player hand :", (0, 350), 32, "White")
    player.draw(canvas, [200, 300])
    
    canvas.draw_text("dealer hand :", (0, 250), 32, "white")
    dealer.draw(canvas, [200, 200])
    if in_play:
        canvas.draw_image(card_back, (36, 48), (72, 96), [200 + CARD_SIZE[0] / 2, 200 + CARD_SIZE[1] / 2], (72, 96), 0)
    
    canvas.draw_text(str(score), (500, 50), 32, "white")
        
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
