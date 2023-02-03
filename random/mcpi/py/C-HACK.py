import os
thing = input("Activate or deactivate the Creative Hack? (a/d) >>> ")
if thing.lower() == "a":
	os.system("sudo cp /home/pi/libhackgmc.so /opt/minecraft-pi-reborn-client/mods/libhackgmc.so")
	input("Done! Press (Enter) to quit.")
elif thing.lower() == "d":
	os.system("sudo rm /opt/minecraft-pi-reborn-client/mods/libhackgmc.so")
	input("Done! Press (Enter) to quit.")