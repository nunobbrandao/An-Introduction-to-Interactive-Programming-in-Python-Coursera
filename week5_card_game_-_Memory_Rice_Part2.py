#import

import simplegui
import random

#inicialize the game
def new_game():
    global state,ticks,initial_list,index_add
    state=0 									# number of cards turned up
    ticks=1										# number of cards flipped
    index_add=[] 								#list that holds the list of index flipped successfully
    initial_list=list(range(1,9)+range(1,9)) 	#initial list of random numbers from 1 to 8
    random.shuffle(initial_list) 				#shuffle the list

#define event handlers
def mouseclick(pos):
    global state,ticks,index_add
    ind=pos[0]//50													#gives the index based on where the click was performed
    if ind not in index_add:										#does not run if position not already in index_add
        if state == 0:													
            index_add.append(ind)									#incr the index_add
            state=1
        elif state == 1:									
            index_add.append(ind)
            state=2
        else:
            if initial_list[index_add[-1]]!=initial_list[index_add[-2]]: #if the last 2 numbers are different remove from index add
                index_add=index_add[0:-2]
            index_add.append(ind)
            state=1
            ticks+=1
    lab.set_text("Turns = "+str(ticks))
    
#draw cards 50x100 pixels in size
def draw(canvas):
    [canvas.draw_polygon([(50*x, 0), (50*x, 100), 
                    (50+50*x, 100),(50+50*x, 0)], 1, 'Brown','Green') 
                    for x,number in enumerate(initial_list) if x not in index_add]
    
    [canvas.draw_text(str(initial_list[x]), [50/4+50*x, 65],
                    50, 'white') for x in index_add]
        
#create frame and button and labels
frame=simplegui.create_frame("Memory",800,100)
frame.add_button("Restart",new_game)
lab=frame.add_label("Turns = 0")

#register event handler
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

#start
new_game()
frame.start()

    
