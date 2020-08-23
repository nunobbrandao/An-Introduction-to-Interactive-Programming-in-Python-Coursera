#import
import simplegui

#define global variables
t = 0
wins = 0
attempts =0

#function format(t). Format converts an integer into
#tenths of seconds in a formatted string A:BD.D
def format(t):
    t=str(t)
    sec =tens = mins = "0"
    tenths=t[-1]
    if len(t)>1:
        sec = t[-2]
    if len(t)>2:
        tens = t[-3]
    if len(t)>3:
        mins = t[:-3]
    return mins+":"+tens+sec+"."+tenths 

#define event handler for buttons; start stop and reset
def start_handler():
    timer.start()

def stop_handler():
    global t, wins,attempts
    timer.stop()
    if str(t)[-1] == "0":
        wins+=1
    attempts+=1

def reset_handler():
    global t, wins, attempts
    f.start()
    t=0
    wins=0
    attempts=0
    
#define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t+=1
    
#define event handler for canvas
def draw_handler(canvas):
    canvas.draw_text(format(t), (50, 115), 40, 'White')
    canvas.draw_text(str(wins)+"/"+str(attempts), (165, 20), 20, 'White')
    
# Create a frame
f = simplegui.create_frame('Stop Watch', 200, 200)

#register event handlers
f.add_button("Start",start_handler,200)
f.add_button("Stop",stop_handler,200)
f.add_button("Reset",reset_handler,200)
timer = simplegui.create_timer(100, timer_handler)
f.set_draw_handler(draw_handler)

#start frame
f.start()