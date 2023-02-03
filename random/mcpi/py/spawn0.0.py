from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()


from pynput.keyboard import *

keys = [KeyCode.from_char(c) for c in 'f']
def on_press(key):
        if key in keys:
            x, y, z = mc.player.getPos()
            print(f'good key: {key}')
            mc.setBlock(x, y, z, 8)
        else:
            print(f'bad key: {key}')

def on_release(key):
        if key==Key.esc:
            return False

while True:

    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

