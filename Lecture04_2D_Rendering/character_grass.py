from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)

x = 0
while x < 800:
      # Game Rendering (그림을 그리는 일)
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(x, 90)

      # Game Logic (게임 내의 객체 상태를 바꿔주는 것)
      x += 2
      
      delay(0.01)
      

close_canvas()
