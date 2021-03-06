
import simplegui
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if not direction:
        ball_vel = [- random.randrange(120,240)/60,- random.randrange(60,180)/60]
    else:
        ball_vel = [random.randrange(120,240)/60,random.randrange(60,180)/60]
        
    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    
    spawn_ball(random.choice([LEFT,RIGHT]))

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "Blck")
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_text(str(score1), [WIDTH/4, 50], 50, "White")
    canvas.draw_text(str(score2), [WIDTH/4*3, 50], 50, "White")
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
        
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT -1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos  <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT and ball_pos[0] < WIDTH/2: 
            ball_pos[0] = BALL_RADIUS + PAD_WIDTH
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.1
            ball_vel[1] += ball_vel[1]*0.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
       
    if ball_pos[0] >= (WIDTH - PAD_WIDTH -1) - BALL_RADIUS: 
        if paddle2_pos  <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT and ball_pos[0] > WIDTH/2: 
            ball_pos[0] = (WIDTH - PAD_WIDTH -1) - BALL_RADIUS
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += ball_vel[0]*0.1
            ball_vel[1] += ball_vel[1]*0.1
        else:
            score1 += 1
            spawn_ball(LEFT)
        
 
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos < 0:  
        paddle1_pos = 0
    elif paddle1_pos + PAD_HEIGHT > HEIGHT:
        paddle1_pos = HEIGHT - PAD_HEIGHT  
    if paddle2_pos < 0:  
        paddle2_pos = 0
    elif paddle2_pos + PAD_HEIGHT > HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT  

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0

frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
restart_button = frame.add_button("Restart game",new_game, 120)

new_game()
frame.start()

