from pico2d import *


def handle_events():
    global running
    global dir
    global num
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                num = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                num = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                num = 3
                dir -= 1
            elif event.key == SDLK_LEFT:
                num = 2
                dir += 1
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0 # -1: left / +1: right

num = 2 # 0: left run / 1: right run / 2: left / 3: right

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * num, 100, 100, x, 90)
    update_canvas()

    handle_events()
    x += dir * 10
    frame = (frame + 1) % 8

    delay(0.02)

close_canvas()

