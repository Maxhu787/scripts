#Scaffold / ScaffoldWalk Module

import minecraft.minecraft as minecraft
import minecraft.block as block
import time

def roundVec3(vec3):
    return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

if __name__ == "__main__":

    print "Loading Module Please wait..."

    time.sleep(2)

    mc = minecraft.Minecraft.create()

    print "Scaffold Activated"
    time.sleep(0.5)
    print "Ctrl+C to Cancel"
    
    lastPlayerPos = mc.player.getPos()

    while (True):

        playerPos = mc.player.getPos()

        movementX = lastPlayerPos.x - playerPos.x
        movementZ = lastPlayerPos.z - playerPos.z

        if ((movementX < -0.2) or (movementX > 0.2) or (movementZ < -0.2) or (movementZ > 0.2)):
            
            nextPlayerPos = playerPos
            while ((int(playerPos.x) == int(nextPlayerPos.x)) and (int(playerPos.z) == int(nextPlayerPos.z))):
                nextPlayerPos = minecraft.Vec3(nextPlayerPos.x - movementX, nextPlayerPos.y, nextPlayerPos.z - movementZ)
            
            blockBelowPos = roundVec3(nextPlayerPos)
            if blockBelowPos.z < 0: blockBelowPos.z = blockBelowPos.z - 1
            if blockBelowPos.x < 0: blockBelowPos.x = blockBelowPos.x - 1
            blockBelowPos.y = blockBelowPos.y - 1
            if mc.getBlock(blockBelowPos) == block.AIR:
                mc.setBlock(blockBelowPos.x, blockBelowPos.y, blockBelowPos.z, block.IRON_BLOCK)

            lastPlayerPos = playerPos

        time.sleep(0.01)
