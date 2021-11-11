#from pico2d import *

num = [1, 2, 3]

for i in range(num):
	yield i

def countdown(num):
	for i in range(num):
		print(i)