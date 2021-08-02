from ursina import *
from PIL import Image, ImageOps # for eventually figuring out how to flip the image

app = Ursina()


class Class1(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube', # built in texture
            rotation = Vec3(45, 45, 45)
        )

class Button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick',
            color = color.green,
            highlight_color = color.cyan,
            pressed_color = color.lime
            )

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                print('click!')


def update():
    running_man.x += held_keys['d'] * .1
    running_man.x -= held_keys['a'] * .1
    running_man.y += held_keys['w'] * .1
    running_man.y -= held_keys['s'] * .1

entity1 = Entity(model = 'quad', color = color.green, scale_y = 1, position = (0,1)) # or scale=(tuple)

# im = Image.open('assets\\running_man.png')
# im_flip= ImageOps.flip(im)
running_man_texture = load_texture('assets\\running_man.png')
running_man = Entity(model = 'quad', texture = running_man_texture, position=(4,4))

# def update():   # update gets automatically called.
#     player.x += held_keys['d'] * .1
#     player.x -= held_keys['a'] * .1

test = Button()

app.run()