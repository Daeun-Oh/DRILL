import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0   # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 5.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:

    def __init__(self):
        Bird.image = load_image('bird100x100x14.png')
        self.frame = 0
        self.x, self.y, self.velocity = random.randint(0, 800), 300, RUN_SPEED_PPS
        self.head = 1

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        # self.velocity += RUN_SPEED_PPS
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        # self.frame += 1
        # if self.frame > 13:
        #     self.frame = 0
        # self.x += 1
        if self.x == 1600:
            self.head = -1
        elif self.x == 0:
            self.head = 1

        if self.head == 1:
            self.x += self.velocity * game_framework.frame_time
        else:
            self.x -= self.velocity * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)