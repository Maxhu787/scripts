import pynput
from time import sleep
from pynput.mouse import Button, Controller
mouse = Controller()
mouse.position
print (mouse.position)
while True:
    mouse.position = (331, 435)
    mouse.click(Button.left, 1)
    sleep(5)
    #mouse.position = (216, 435)
    #mouse.click(Button.left, 1)
    #sleep(3)
    #mouse.position = (331, 435)
    #sleep(1)
    mouse.click(Button.left, 1)
    sleep(3)
    mouse.position = (961, 712)
    mouse.click(Button.left, 1)
    sleep(3)
    mouse.position = (1135, 235)
    mouse.click(Button.left, 1)
    sleep(3)


#mouse.position = (15, 1059)
#mouse.click(Button.left, 10)