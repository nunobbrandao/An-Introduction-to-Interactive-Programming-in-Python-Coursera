# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import random

height=400
width=600
pad_width=8
pad_height=80
ball_radius=20
score1=score2=0

#start function
def new_game():
    global pad1_pos,pad2_pos,pad1_vel,pad2_vel,ball_pos, ball_vel
    global score1,score2
    ball_pos=[width/2,height/2]
    ball_vel=[random.choice([-1,-2,-3,1, 2, 3]),random.choice([-1,-2,-3,1, 2, 3])]
    pad1_pos=[[0, height/2], [pad_width, height/2], 
              [pad_width, height/2+pad_height],
              [0,height/2+pad_height]]
    pad2_pos=[[width-pad_width, height/2], 
              [width, height/2], [width, height/2+pad_height],
              [width-pad_width,height/2+pad_height]]
    pad1_height_centre=(height+pad1_pos[0][0]*2)/2
    pad2_vel=pad1_vel=0

      
# Handler to draw on canvas
def draw(canvas):
    global pad2_vel,pad1_vel,score1,score2
    
    #update ball position and decide whether to continue the game
    ball_pos[1]+=ball_vel[1]
    ball_pos[0]+=ball_vel[0]
    acc=1 						#acceleration when the ball hits the pad
    if ball_pos[1]>=height-ball_radius or ball_pos[1]<=ball_radius:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[0]>=width-ball_radius-pad_width:
        ball_vel[0]=-ball_vel[0]-acc
        if (ball_pos[1]<pad2_pos[0][1] or ball_pos[1]>pad2_pos[2][1]):
            score2+=1
            new_game()
    if ball_pos[0]<=ball_radius+pad_width:
        ball_vel[0]=-ball_vel[0]+acc
        if (ball_pos[1]<pad1_pos[0][1] or ball_pos[1]>pad1_pos[2][1]):
            score1+=1
            new_game()
            
    #update pad positions, keep padle on the screen
    if (pad2_pos[0][1]==0 and pad2_vel<0) or (pad2_pos[2][1]==height and pad2_vel>0)  :
        pad2_vel=0
    if (pad1_pos[0][1]==0 and pad1_vel<0) or (pad1_pos[2][1]==height and pad1_vel>0)  :
        pad1_vel=0
    for i in pad1_pos:
        i[1]=i[1]+pad1_vel
    for i in pad2_pos:
        i[1]=i[1]+pad2_vel
        
    #draw pads
    canvas.draw_polygon(pad1_pos, 1, 'white','white')
    canvas.draw_polygon(pad2_pos, 1, 'white','white')
    
    #draw ball
    canvas.draw_circle(ball_pos, ball_radius,.1,'white', 'white')
    
    #draw lines
    canvas.draw_line((pad_width, 0), (pad_width, height), 1, 'white')
    canvas.draw_line((width-pad_width, 0), (width-pad_width, height), 1, 'white')
    canvas.draw_line((width/2, 0), (width/2, height), 1, 'white')
    
    #draw scores
    canvas.draw_text(str(score2), [width/2+10, 50], 50, 'White')
    canvas.draw_text(str(score1), [width/2-40, 50], 50, 'White')

# Handler for pad control
def key_handler_down(key):
    global pad2_vel,pad1_vel
    if simplegui.KEY_MAP['down']==key:
        pad2_vel+=5
    elif simplegui.KEY_MAP['up']==key:
        pad2_vel-=5
    if simplegui.KEY_MAP['s']==key:
        pad1_vel+=5
    elif simplegui.KEY_MAP['w']==key:
         pad1_vel-=5

def key_handler_up(key):
    global pad2_vel,pad1_vel
    if simplegui.KEY_MAP['down']==key:
        pad2_vel=0
    elif simplegui.KEY_MAP['up']==key:
        pad2_vel=0
    elif simplegui.KEY_MAP['s']==key:
        pad1_vel=0
    elif simplegui.KEY_MAP['w']==key:
        pad1_vel=0
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_handler_down)
frame.set_keyup_handler(key_handler_up)

# Start the frame animation
frame.start()
new_game()
