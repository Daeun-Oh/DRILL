'''
상태(state): 어떤 조건을 만족하는 동안의 상황
이벤트(event): 상태 변화를 일으키는 일
Entry action: 어떤 상태로 들어갈 때 발생하는 일
Exit action: 어떤 상태에서 나갈 때 발생하는 
Do activity: 특정 상태에 머무르는 동안 수행하는 일(반복될 수 있다.)
'''
from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, RIGHT_SHIFT, LEFT_SHIFT, DASH_TIMER = range(8) # 0부터 3까지의 정수값이 차례로 할당됨.

key_event_table = {
    # Key는 (정수, 정수) tuple   # Value는 정수
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): RIGHT_SHIFT,
    (SDL_KEYDOWN, SDLK_LSHIFT): LEFT_SHIFT
    # 입력 키값 해석을 단순화시키고, 키입력을 단일이벤트로 만들기 위한 매핑
    # 오른쪽 키가 눌렸다 / 왼쪽 키가 눌렸다 / 오른쪽 키가 떼어졌다 / 왼쪽 키가 떼어졌다
}

# Boy States
class IdleState:
    # Entry Action
    def enter(boy, event):  # 이벤트 전달 받음
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000

    # Exit Action
    def exit(boy, event):
        pass

    # Do Activity
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity  # 방향을 현재 방향으로 맞춰준다.

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class SleepState:
    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)

        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class DashState:
    def enter(boy, event):
        if event == RIGHT_SHIFT or LEFT_SHIFT:
            boy.timer = 150

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity * 2
        boy.x = clamp(25, boy.x, 800 - 25)
        if boy.timer == 0:
            boy.add_event(DASH_TIMER)

    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

next_state_table = {
    # 모든 경우를 생각. ex) 깨어있는데 때리면?, 자고있는데 10초가 지나면?
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, LEFT_SHIFT: IdleState, RIGHT_SHIFT: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, LEFT_SHIFT: DashState, RIGHT_SHIFT: DashState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, LEFT_SHIFT: SleepState, RIGHT_SHIFT: SleepState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, DASH_TIMER: RunState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []         # 이벤트 큐 초기화
        self.cur_state = IdleState  # 현재 상태: IdleState
        self.cur_state.enter(self, None) # entry action 실행


    def change_state(self, state):
        pass

    def add_event(self, event):
        self.event_que.insert(0, event)


    def update(self):
        self.cur_state.do(self) # 현재 상태의 Do Activity 수행

        # 이벤트가 있으면 현재 상태의 Exit Action 수행. 다음 상태 계산. 다음 상테의 Entry Action 수행.
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + ' Dir:' + str(self.dir))


    # 입력된 키와 눌린 상태를 해석해서 이벤트를 만들고 이벤트 큐에 추가
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

