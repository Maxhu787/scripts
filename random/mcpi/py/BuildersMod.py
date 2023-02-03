from mcpi.minecraft import Minecraft

'#Wallee'

mc = Minecraft.create()
x, y, z = mc.player.getPos()

while True:

    ID = 0
    for hitBlock in mc.events.pollBlockHits():

        x = hitBlock.pos.x
        y = hitBlock.pos.y
        z = hitBlock.pos.z

        ID, mdata = mc.getBlockWithData(x, y, z)

    '#wood'
    if ID == 17:
        mdata += 1
        if mdata == 3:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#reactor'
    if ID == 247:
        mdata += 1
        if mdata == 3:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#wool'
    if ID == 35:
        mdata += 1
        if mdata == 16:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#artificial leaves'
    if ID == 18:
        mdata += 1
        if mdata == 11:
            mdata = 8
        mc.setBlock(x, y, z, ID, mdata)

    '#saplin'
    if ID == 6:
        mdata += 1
        if mdata == 3:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#tall grass'
    if ID == 31:
        mdata += 1
        if mdata == 2:
            ID = 30
        mc.setBlock(x, y, z, ID, mdata)
    if ID == 30:
        mc.setBlock(x, y, z, ID, 31)

    '#cobweb'
    if ID == 30:
        if mdata == 0:
            ID = 31
        if mdata == 2:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#stone brick'
    if ID == 98:
        mdata += 1
        if mdata == 3:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#tnt'
    if ID == 46:
        mdata += 1
        if mdata == 1:
            mc.postToChat("Active")
        if mdata == 2:
            mdata = 0
            mc.postToChat("Inactive")
        mc.setBlock(x, y, z, ID, mdata)

    '#sandstone'
    if ID == 24:
        mdata += 1
        if mdata == 3:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#laddar/chestd'
    if ID == 65 or ID == 54:
        mdata += 1
        if mdata == 6:
            mdata = 2
        mc.setBlock(x, y, z, ID, mdata)

    '#dirt/grass/[FRAMLAND]/sand/gravel/clay'
    if ID == 2 or ID == 3 or ID == 12 or ID == 13 or ID == 82:
        ID += 1
        if ID == 4:
            ID = 60
            mdata = -7
        if ID == 14:
            ID = 82
        if ID == 83:
            ID = 2
        mc.setBlock(x, y, z, ID)

    '#farmland'
    if ID == 60:
        mdata += 7
        if mdata == 14:
            mdata = 0
            ID = 12
        mc.setBlock(x, y, z, ID, mdata)

    '#quartz'
    if ID == 155:
        mdata += 1
        if mdata == 3:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#flowers/mushrooms'
    if ID == 37 or ID == 38 or ID == 39 or ID == 40:
        ID += 1
        if ID == 41:
            ID = 37
        mc.setBlock(x, y, z, ID, mdata)

    '#melon seed'
    if ID == 105:
        mdata += 1
        if mdata == 8:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#seeds'
    if ID == 59:
        mdata += 1
        if mdata == 8:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#cobblestone'
    if ID == 4 or ID == 48:
        if ID == 4:
            ID = 48
        else:
            ID = 4
        mc.setBlock(x, y, z, ID)

    '#obsidian/glowing obsidian/bedrock'

    if ID == 7 or ID == 49 or ID == 246:
        ID += 1
        if ID == 8:
            ID = 49
        if ID == 50:
            ID = 246
        if ID == 247:
            ID = 7
        mc.setBlock(x, y, z, ID)

    '#stairs'
    if ID == 53 or ID == 67 or ID == 108 or ID == 109 or ID == 114 or ID == 128 or ID == 156:
        mdata += 1
        if mdata == 8:
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#stone slab'
    if ID == 44 and mdata == 0 or ID == 44 and mdata == 8 or ID == 43 and mdata == 0 or ID == 43 and mdata == 6:
        mdata += 8
        if ID == 43:
            if mdata == 14:
                ID = 44
                mdata = 0
            else:
                mdata = 6

        if ID == 44 and mdata == 16:
            ID = 43
            mdata = 0
        mc.setBlock(x, y, z, ID, mdata)

    '#sandstone slab'
    if ID == 44 and mdata == 1 or ID == 44 and mdata == 9 or ID == 43 and mdata == 1:
        mdata += 8
        if ID == 43:
            ID = 44
            mdata = 1
        if ID == 44 and mdata == 17:
            ID = 43
            mdata = 1
        mc.setBlock(x, y, z, ID, mdata)

    '#wooden slab'
    if ID == 44 and mdata == 2 or ID == 44 and mdata == 10 or ID == 43 and mdata == 2:
        mdata += 8
        if ID == 43:
            ID = 44
            mdata = 2
        if ID == 44 and mdata == 18:
            ID = 43
            mdata = 2
        mc.setBlock(x, y, z, ID, mdata)

    '#cobblestone slab'
    if ID == 44 and mdata == 3 or ID == 44 and mdata == 11 or ID == 43 and mdata == 3:
        mdata += 8
        if ID == 43:
            ID = 44
            mdata = 3
        if ID == 44 and mdata == 19:
            ID = 43
            mdata = 3
        mc.setBlock(x, y, z, ID, mdata)

    '#bircks slab'
    if ID == 44 and mdata == 4 or ID == 44 and mdata == 12 or ID == 43 and mdata == 4:
        mdata += 8
        if ID == 43:
            ID = 44
            mdata = 4
        if ID == 44 and mdata == 20:
            ID = 43
            mdata = 4
        mc.setBlock(x, y, z, ID, mdata)

    '#stone bricks slab'
    if ID == 44 and mdata == 5 or ID == 44 and mdata == 13 or ID == 43 and mdata == 5:
        mdata += 8
        if ID == 43:
            ID = 44
            mdata = 5
        if ID == 44 and mdata == 21:
            ID = 43
            mdata = 5
        mc.setBlock(x, y, z, ID, mdata)