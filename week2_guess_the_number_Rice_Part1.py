# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

#import
import simplegui
import random
import math

#variables
#variable i counts the number of attempts


#Functions

def new_game():
    range_100()

def function_range(low,high,n_tries):
    i=0
    computer=random.randint(low, high)
    print "New game, range is from ", low," to ", high
    print "Number of remaining guesses is ", n_tries
    print " "
    return i,computer
    
def range_100():
    global computer, n_tries,i
    high = 100
    low=0
    n_tries = 7
    i,computer = function_range(low,high,n_tries)
    
def range_1000(): 
    global computer, n_tries,i
    high = 1000
    low=0
    n_tries = 10
    i,computer = function_range(low,high,n_tries)

def get_input(guess):
    global i
    guess = int(guess)
    if i<n_tries:
        i+=1
        print "Guess was ", guess
        print "number of remaining guesses is ", n_tries-i
        if guess < computer:
            print "Higher"
        elif guess >computer:
            print "Lower"
        else:
            print "Correct!"
            print " "
            new_game()
            i=0
    if i==n_tries :
        print "you run out of guesses. The correct number was ",computer
        print " "
        new_game()
        i=0
    print " "
    
# Create a frame
f = simplegui.create_frame('Wonder the number', 200, 200)
#Handler 
f.add_button("Range is [0,100]",range_100,200)
f.add_button("Range is [0,1000]",range_1000,200)
f.add_input("Enter a guess",get_input,200)    
#start frame
f.start()

new_game()

# Start the frame & timers

