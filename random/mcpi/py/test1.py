from mcpi.minecraft import Minecraft
mc = Minecraft.create()
entityIds = mc.getPlayerEntityIds()
print(entityIds)
input = input("The first, the second, the third ...? ")
input = int(input)
input = input - 1
result = mc.entity.getTilePos(entityIds[input])
#print(result)
mc.postToChat("result")