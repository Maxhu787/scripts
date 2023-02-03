from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
entityIds = mc.getPlayerEntityIds()
while True:
    result = mc.entity.getTilePos(entityIds[0])
    mc.postToChat(result)
    sleep(1)
    
    