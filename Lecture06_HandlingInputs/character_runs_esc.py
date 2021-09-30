from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    global running

    events = get_events()
    for event in events:
        # 윈도우 창의 x키 누르면 종료
        if event.type == SDL_QUIT:
            running = False
        # ESC키를 누르면 종료
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    pass


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.01)

close_canvas()

