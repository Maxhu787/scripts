from mcpi.minecraft import Minecraft

'#Wallee'
'#stoped working but I "fixed" it'

mc = Minecraft.create()
x, y, z = mc.player.getPos()

'#Chat messages [True/False]'

chat = False


'#get the area to clear'

def getArea():
    checker = 0
    while checker == 0:
        for hitBlock in mc.events.pollBlockHits():

            x = hitBlock.pos.x
            y = hitBlock.pos.y
            z = hitBlock.pos.z

            checker, mdata = mc.getBlockWithData(x, y, z)

    return(x, y, z)


'#conform clearing'

def conform(x2, y2, z2):
    block = mc.getBlockWithData(x2, y2, z2)
    mc.setBlock(x2, y2, z2, 247, 2)
    keepBlock = 0
    fill = 0
    data = 0
    while keepBlock == 0:
        for hitBlock in mc.events.pollBlockHits():

            x = hitBlock.pos.x
            y = hitBlock.pos.y
            z = hitBlock.pos.z

            keepBlock = mc.getBlock(x, y, z)

            if {x, y, z} != {x2, y2, z2}:
                fill, data = mc.getBlockWithData(x, y, z)

        if mc.getBlock(x2, y2, z2) != 247:
            keepBlock = -1

    mc.setBlock(x2, y2, z2, block)
    return(keepBlock, block, fill, data)


'#creat loop'

while True:
    '#get both positions'

    x1, y1, z1 = getArea()
    x2, y2, z2 = getArea()

    '#get conformation'

    if chat:
        mc.postToChat("Right click to Cancel")
        mc.postToChat("Left click to Clear area")
        mc.postToChat("Left click seperate block to fill")

    keepBlock, block, fill, data = conform(x2, y2, z2)

    '#finish task'

    if keepBlock == -1:
        mc.setBlocks(x1, y1, z1, x2, y2, z2, 0)

    if fill != 0:
        mc.setBlocks(x1, y1, z1, x2, y2, z2, fill, data)