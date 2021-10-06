from pico2d import *
from random import *


def handle_events():
    global running
    global dir
    global num
    global hand_x, hand_y, character_x, character_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

    if character_x == hand_x and character_y == hand_y:
        hand_x = randint(0, 800)
        hand_y = randint(0, 600)

    if character_x < hand_x:
        num = 1
    else:
        num = 0

    character_x = hand_x
    character_y = hand_y

    # if character_x != hand_x and character_y != hand_y:
    #     if character_x < hand_x:
    #         character_x += 1
    #         if  character_y < hand_y:
    #             character_y += 1
    #     elif character_x > hand_x:
    #         character_x -= 1
    #         if  character_y < hand_y:
    #             character_y += 1
    #     elif character_x < hand_x:
    #         character_x += 1
    #         if  character_y > hand_y:
    #             character_y -= 1
    #     elif character_x > hand_x:
    #         character_x -= 1
    #         if  character_y > hand_y:
    #             character_y -= 1
        

    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x = 800 // 2
frame = 0
dir = 0

num = 2

hand_x = randint(0, 800)
hand_y = randint(0, 600)

character_x = x
character_y = 90

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * num, 100, 100, character_x, character_y)
    hand.draw(hand_x, hand_y)
    update_canvas()

    handle_events()
    x += dir * 10
    frame = (frame + 1) % 8

    delay(0.5)

close_canvas()