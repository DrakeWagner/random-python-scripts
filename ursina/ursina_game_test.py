from ursina import *

app = Ursina()

def update():
    if held_keys['a']:
        entity1.x -= .1 * time.dt

entity1 = Entity(model = 'quad', color = color.green, scale_y = 1, position = (0,1)) # or scale=(tuple)


sans_texture = load_texture()
sans = Entity(model = 'quad', textture = )

# def update():   # update gets automatically called.
#     player.x += held_keys['d'] * .1
#     player.x -= held_keys['a'] * .1

app.run()