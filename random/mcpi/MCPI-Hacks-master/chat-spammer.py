# ChatSpammer / ChatSpam Module

from minecraft.minecraft import Minecraft
import time
mc = Minecraft.create()

print "Loading Module Please wait..."

def chat_spammer():
	mc.postToChat("Hello world")

time.sleep(5)
print"ChatSpammer Activated"
time.sleep(0.5)
print "Ctrl+C to Cancel"

while True:
	chat_spammer()
	time.sleep(1)
