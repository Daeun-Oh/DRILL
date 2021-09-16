import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

x = 400
y = 90
cnt = 0
   

while(True):
      if cnt == 0 or cnt == 1:
            if x < 800 and y == 90:
                  if x == 400 and cnt ==1:
                        cnt = 2
                        continue
                  clear_canvas_now()
                  grass.draw_now(400, 30)
                  character.draw_now(x, y)
                  x += 2
                  delay(0.005)
            elif x == 800 and y < 600:
                  clear_canvas_now()
                  grass.draw_now(400, 30)
                  character.draw_now(x, y)
                  y += 2
                  delay(0.005)
            elif x > 0 and y == 600:
                  clear_canvas_now()
                  grass.draw_now(400, 30)
                  character.draw_now(x, y)
                  x -= 2
                  delay(0.005)
            elif x == 0 and y > 90:
                  clear_canvas_now()
                  grass.draw_now(400, 30)
                  character.draw_now(x, y)
                  y -= 2
                  delay(0.005)
                  cnt = 1

      if cnt == 2:
            for i in range(90, 90 + 360 + 1):
                  if i == 90 + 360:
                        x = 400
                        y = 90
                        cnt = 0
                        continue
                  clear_canvas_now()
                  grass.draw_now(400, 30)
                  character.draw_now(400 + 210 * math.cos(math.radians(i)), 300 + 210 * math.sin(math.radians(i)))
                  delay(0.005)
close_canvas()
