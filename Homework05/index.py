import simplegui
import random
import math


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 100
CARDS_NUMBER = 16

CARD_PLACEHOLDER_WIDTH = (CANVAS_WIDTH // CARDS_NUMBER)

FONT_SIZE = 50 
FONT_FACE = 'sans-serif'
FONT_COLOR = 'White'
MARGIN_Y = 19

CARD_VALUE_POINT_Y = (CANVAS_HEIGHT // 2) + MARGIN_Y 

CARD_PLACEHOLDER_LINE_COLOR = 'Red'
CARD_PLACEHOLDER_FILL_COLOR = 'Black'
CARD_PLACEHOLDER_LINE_WIDTH = 3

def new_game():
    global deck_of_cards
    deck_of_cards = range(CARDS_NUMBER // 2) + range(CARDS_NUMBER // 2)

    random.shuffle(deck_of_cards)
    global deck_of_cards_exposed
    deck_of_cards_exposed = [False] * CARDS_NUMBER
    
    global state
    state = 0  
    
    global turn 
    turn = 0
    label.set_text("Turns = " + str(turn))

    global index_of_cards_exposed_in_a_turn 
    index_of_cards_exposed_in_a_turn = [-1, -1]
    
    return None


def mouseclick(pos):
   
    clicked_card_index = int(math.floor(float(pos[0]) / CARD_PLACEHOLDER_WIDTH))
    

    if deck_of_cards_exposed[clicked_card_index]:
        return None
    

    global turn

    global state  
    if state == 0:
       
        deck_of_cards_exposed[clicked_card_index] = True
        
       
        index_of_cards_exposed_in_a_turn[0] = clicked_card_index
        
       
        turn += 1
        label.set_text("Turns = " + str(turn))
        
       
        state = 1
    elif state == 1:
          
        deck_of_cards_exposed[clicked_card_index] = True

      
        index_of_cards_exposed_in_a_turn[1] = clicked_card_index
        
       
        state = 2
    else:
       
        deck_of_cards_exposed[clicked_card_index] = True

       
        if deck_of_cards[index_of_cards_exposed_in_a_turn[0]] != deck_of_cards[index_of_cards_exposed_in_a_turn[1]]:
            deck_of_cards_exposed[index_of_cards_exposed_in_a_turn[0]] = False
            deck_of_cards_exposed[index_of_cards_exposed_in_a_turn[1]] = False
        

        index_of_cards_exposed_in_a_turn[0] = clicked_card_index
      

        turn += 1
        label.set_text("Turns = " + str(turn))
        
        state = 1
                
    return None   

def draw(canvas):
     
    for index in range(CARDS_NUMBER):
      
        card_placeholder_left_x = CARD_PLACEHOLDER_WIDTH * index
        card_placeholder_right_x = CARD_PLACEHOLDER_WIDTH * (index + 1)
        
     
        if deck_of_cards_exposed[index]:
        
            card_placeholder_middle_x = (card_placeholder_right_x + card_placeholder_left_x) // 2 
            card_value_textwidth_in_px = frame.get_canvas_textwidth(str(deck_of_cards[index]), 
                                                                        FONT_SIZE, FONT_FACE)   
            card_value_point_x = card_placeholder_middle_x - (card_value_textwidth_in_px // 2)     
           
            canvas.draw_text(str(deck_of_cards[index]), (card_value_point_x, CARD_VALUE_POINT_Y), 
                                 FONT_SIZE, FONT_COLOR, FONT_FACE)
                        
        else:
            card_placeholder_points = [[card_placeholder_left_x, 0], 
                                       [card_placeholder_right_x, 0], 
                                       [card_placeholder_right_x, CANVAS_HEIGHT], 
                                       [card_placeholder_left_x, CANVAS_HEIGHT]]
           
            canvas.draw_polygon(card_placeholder_points, 
                                CARD_PLACEHOLDER_LINE_WIDTH, 
                                CARD_PLACEHOLDER_LINE_COLOR, 
                                CARD_PLACEHOLDER_FILL_COLOR)   	     
    
    return None

frame = simplegui.create_frame("Memory", CANVAS_WIDTH, 
                               CANVAS_HEIGHT)


frame.add_button("Reset", new_game)
frame.add_label("")
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)

frame.set_draw_handler(draw)


new_game()

frame.start()
