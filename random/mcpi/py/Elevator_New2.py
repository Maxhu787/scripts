from mcpi.minecraft import Minecraft
import time
print('Hello, thank you for using my elevator script! - Wallee')

mc = Minecraft.create()
height = 10  #set range of elevator
blockID = 35  #set block of elevator

while True:
    x, y, z = mc.player.getPos()
    y+=70
    '#Going Down'
    if y-int(y) > 0.79:
        block, mData = mc.getBlockWithData(x, y-70, z)
        if block == blockID:
            for i in range(3, height):
                blockCH, mDataCheck = mc.getBlockWithData(x, y-i-71, z)
                if blockCH == blockID and mData == mDataCheck:
                    mc.player.setPos(x, y-i+0.2-70, z)
                    time.sleep(0.5)

    '#Going Up'
    if y-int(y) >= 0.1:
        block, mData = mc.getBlockWithData(x, y-71, z)
        if block == blockID:
            for i in range(3, height):
                blockCH, mDataCheck = mc.getBlockWithData(x, y+i-70, z)
                if blockCH == blockID and mData == mDataCheck:
                    mc.player.setPos(x, int(y+i-70)+1.2, z)
                    time.sleep(0.5)
                    break
