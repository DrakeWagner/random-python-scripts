import random
import time
from mcpi import minecraft
mc = minecraft.Minecraft.create()

flower = 38
while True:
    x, y, z = mc.player.getPos()
    mc.setBlock(x, y, z, flower)
    time.sleep(0.1)
