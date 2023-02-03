import mcpi.minecraft
from mcpi import block
mc = mcpi.minecraft.Minecraft.create()

while True:
    x, y, z = mc.player.getPos()
    mc.setBlocks(x-1, y-1, z-1, x+1, y-1, z+1,block.WATER.id)
    #mc.setBlocks(x-2, y-1, z-1, x-2, y-1, z+1, 0)
    #mc.setBlocks(x+2, y-1, z-1, x+2, y-1, z+1, 0)

    #mc.setBlocks(x-1, y-1, z-2, x+1, y-1, z-2, 0)
    #mc.setBlocks(x-1, y-1, z+2, x+1, y-1, z+2, 0)
    #mc.setBlocks(x-2, y, z-2, x+2, y+1, z+2, 0)
    #mc.setBlocks(x-2, y-2, z-2, x+2, y-2, z+2, 0)   