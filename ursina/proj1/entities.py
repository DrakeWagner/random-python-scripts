from ursina import *
from random import *

app = Ursina()

window.borderless = False
window.title = 'Drake World'
window.color = color.black
window.show_ursina_splash = False

class Player(Entity):

	def __init__(self):
		super().__init__()
		self.model='cube'
		self.rotation=(0,0,0)
		self.color = color.lime
		self.scale = (2,2,2)
		self.position = (0,0,0)


Text(text= 'test', 
	origin=(20,20), 
	background=True
	)


def input(key):
	if key == 'a':
		print('test')
		test.text = 'TEST TEXT'
		print(test.text)


player = Player()

iter = 0
speed = 2

def update():
	global iter
	global speed

	iter += 1

	player.x=player.x+time.dt*speed*randint(-1,1)
	player.y=player.y+time.dt*speed*randint(-1,1) # movements
	player.rotation_x=player.rotation_x+time.dt
	player.rotation_y=player.rotation_y+time.dt*10

	red=randint(0,255)
	green=randint(0,255)
	blue=randint(0,255)

	if iter % 25 == 5:
		player.color=color.rgb(red,green,blue)

	player.rotation_x=player.rotation_x+time.dt*(randint(-50,150))
	player.rotaiton_y=player.rotation_y+time.dt*(randint(-50,150))


	# movement boundary
	if abs(player.x) > 5 or abs(player.y) > 5:
		# invert/have bounce off border like DVD?
		player.x=player.x+time.dt*speed*randint(-1,1) #*(randint(-100,100)/100)
		player.y=player.y+time.dt*speed*-1
		print(player.x*100, player.y*100)
		player.position=0
		speed = randint(-2,2)

app.run()
