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
        canvas.draw_image(card_images, card_loc, CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):      
        self.hand=[]       
    
    def __str__(self): 
        s = [str(i) for i in self.hand]
        return "Hand contains " + str(s) 

    def add_card(self, card):
        self.hand.append(card)	

    def get_value(self):
        self.value=0
        for i in self.hand:
            if  (str(i)[1]=='A') and (self.value+11<=21): 
                self.value +=11
            else:
                self.value += VALUES[str(i)[1]]
        return self.value     
    
    def draw(self, canvas, pos):
        for i in self.hand:
            card=Card(i[0],i[1])
            card.draw(canvas,pos)
            pos[0]+=CARD_SIZE[0]

# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for i in SUITS:
            for j in RANKS:
                self.deck.append(i+j)
    
    def __str__(self):
        s = [str(i) for i in self.deck]
        return str(s) 	
                
    def shuffle(self):
        random.shuffle(self.deck) 

    def deal_card(self):
        card=self.deck[-1]
        self.deck=self.deck[0:-1]
        return card 

#define event handlers for buttons
def deal():
    global outcome, in_play, hand_player,hand_dealer,deck

    deck = Deck()
    deck.shuffle()
    
    hand_player=Hand()
    hand_player.add_card(deck.deal_card())
    hand_player.add_card(deck.deal_card())

    
    hand_dealer=Hand()
    hand_dealer.add_card(deck.deal_card())
    hand_dealer.add_card(deck.deal_card()) 
    
    in_play = True	
    
    outcome = "Hit or Stand?"
    

def hit():
    global hand_player,hand_dealer,deck,score,in_play,outcome
    
    if in_play==True:
        
        if hand_player.get_value()<21:
            hand_player.add_card(deck.deal_card()) 
            outcome = "Hit or Stand?"
        
        elif hand_player.get_value()>21:
            print "you've busted"
            outcome = "New deal?"
            score-=1
            in_play=False

def stand():
    global hand_player,hand_dealer,score,in_play,outcome
    
    if in_play==True: 
        while hand_dealer.get_value()<17:
            hand_dealer.add_card(deck.deal_card())

        if (hand_dealer.get_value()>21 or hand_dealer.get_value()<hand_player.get_value()):
            print "Dealer has busted"
            score+=1    
        elif in_play==True:
            score-=1

    in_play=False
    outcome = "New deal?"


# draw handler    
def draw(canvas):
    hand_dealer.draw(canvas, [100, 200])
    hand_player.draw(canvas, [100, 400])
    if in_play==True:
        canvas.draw_image(card_back,CARD_BACK_CENTER, CARD_BACK_SIZE ,[100+72/2, 200+96/2],CARD_BACK_SIZE)
    canvas.draw_text("score: " +str(score), (400,100), 52, 'Red')
    canvas.draw_text("Dealer:", [100, 175], 34, 'Black')
    canvas.draw_text("Player:", [100, 375], 34, 'Black')
    canvas.draw_text(outcome, [400, 375], 34, 'Black')

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
