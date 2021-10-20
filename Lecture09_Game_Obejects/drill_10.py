from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball_s:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 599

    def update(self):
        if self.y > 60+21/2:
            self.y -= random.randint(1, 6)
        else:
            pass

    def draw(self):
            self.image.draw(self.x, self.y)

class Ball_l:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599

    def update(self):
        if self.y > 60+21/2:
            self.y -= random.randint(1, 6)
        else:
            pass

    def draw(self):
            self.image.draw(self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



# initialization code

open_canvas()

grass = Grass()
# boy = Boy()
# ball = Ball_s()

num = random.randint(0, 20+1)

team = [Boy() for i in range(11)]
ballS = [Ball_s() for i in range(num)]
ballL = [Ball_l() for i in range(20 - num)]

running = True

# game main loop code

while running:


    handle_events()

    for boy in team:
        boy.update()

    for ball_s in ballS:
        ball_s.update()

    for ball_l in ballL:
        ball_l.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()

    for ball_s in ballS:
        ball_s.draw()

    for ball_l in ballL:
        ball_l.draw()

    update_canvas()

    delay(0.05)
    

# finalization code
