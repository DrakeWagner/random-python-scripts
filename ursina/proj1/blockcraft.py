# spleef game? high score by time
# high score list

from ursina import *
from ursina.shaders import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

grass_texture = load_texture('assets\\platformPack_tile019.png')
stone_texture = load_texture('assets\\platformPack_tile016.png')
sky_texture = load_texture('assets\\platformPack_tile017.png')
arm_texture = load_texture('assets\\platformPack_tile018.png')
block_pick = 1

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = 'grass'):
            super().__init__(
                parent = scene,
                position = position,
                model = 'cube',
                origin_y = 0.5,
                texture = texture,
                color = color.color(0,0,random.uniform(0.8,1)),
                highlight_color = color.lime.tint(.1),
                scale=1
                )

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                if block_pick == 1:
                    voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture) 
                elif block_pick == 2:
                    voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture) 
                  
            if key == 'right mouse down':
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sphere',
            texture = sky_texture,
            scale = 150,
            double_sided = True,
            shader = normals_shader
            )

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'quad',
            texture = arm_texture,
            scale=50,
            rotation = Vec3(150, -10, 0))

def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2

voxel = Voxel()
for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))
person = FirstPersonController()
hand = Hand()
sky = Sky()
app.run()

