from mcpi.minecraft import Minecraft
mc = Minecraft.create()
entityIds = mc.getPlayerEntityIds()
print(entityIds)
mc.entity.setPos(1390695, -110, -61, -100)
#while True:
    #mc.entity.setPos(1389801, -110, -61, -100)