from pico2d import *
from random import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            # 윈도우 API 좌표계에서 pico2d 좌표계로 변환
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def update_character():
    global x, y
    global ax, ay

    x = (1 - 0.1) * x + 0.1 * ax
    y = (1 - 0.1) * y + 0.1 * ay

    # 캐릭터와 손의 거리 계산
    dist = (ax - x)**2 + (ay - y)**2
    if dist < 10**2:
        ax, ay = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)

open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ax, ay = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)
frame = 0
hide_cursor() # 커서 숨기기

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    arrow.draw(ax, ay)
    update_canvas()
    frame = (frame + 1) % 8

    update_character()

    handle_events()

    get_events()

close_canvas()




