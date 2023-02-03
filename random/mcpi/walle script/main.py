import pygame
from pygame.locals import *
from time import sleep
from PIL import Image

class Canvas():
    def __init__(self):
        image = Image.open("default.png")

        self.import_img = pygame.image.load("import.png").convert()
        self.export_img = pygame.image.load("export.png").convert()
        self.random_img = pygame.image.load("random.png").convert()
        self.reset_img  = pygame.image.load("reset.png").convert()
        self.about_img  = pygame.image.load("about.png").convert()

        self.pixels = {}

        for x in range(64):
            for y in range(32):
                tile = (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pixel = list(image.getpixel((x, y)))
                self.pixels[f'{x}:{y}'] = [tile, pixel]

    def draw(self, screen):
        for x in range(64):
            for y in range(44):
                color = 255 - ((x+y) % 2 == 1) * 60
                pygame.draw.rect(screen, (color, color, color), (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

        for tile in self.pixels:
            rect_alpha = pygame.Surface(pygame.Rect(self.pixels[tile][0]).size, pygame.SRCALPHA)
            pygame.draw.rect(rect_alpha, self.pixels[tile][1], rect_alpha.get_rect())
            screen.blit(rect_alpha, self.pixels[tile][0])

        for x in range(256):
            red   = pygame.Rect(640 + x, 0, 1, 30)
            green = pygame.Rect(640 + x, 30, 1, 30)
            blue  = pygame.Rect(640 + x, 60, 1, 30)
            alpha = pygame.Rect(640 + x, 90, 1, 30)

            pygame.draw.rect(screen, (x, 0, 0, 0), red)
            pygame.draw.rect(screen, (0, x, 0, 0), green)
            pygame.draw.rect(screen, (0, 0, x, 0), blue)

            pix_alpha = pygame.Surface(alpha.size, pygame.SRCALPHA)
            pygame.draw.rect(pix_alpha, (255, 255, 255, 255-x), pix_alpha.get_rect())
            screen.blit(pix_alpha, alpha)

        screen.blit(self.import_img, (640, 120))
        screen.blit(self.export_img, (640, 184))
        screen.blit(self.random_img, (640, 248))
        screen.blit(self.reset_img,  (640, 312))
        screen.blit(self.about_img,  (640, 376))

FPS           = 60
SCREEN_WIDTH  = 895
SCREEN_HEIGHT = 900
TILE_SIZE     = 10

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minecraft: Pi Skin Maker")
clock = pygame.time.Clock()

canvas = Canvas()

run = True

while run:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_y)
    if mouse_y < 320 and mouse_x < 640:
        if pygame.mouse.get_pressed()[0]:
            canvas.pixels[f'{int(mouse_x / TILE_SIZE)}:{int(mouse_y / TILE_SIZE)}'][1] = (0, 0, 0)

        elif pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()
            canvas.pixels[f'{int(mouse_x / TILE_SIZE)}:{int(mouse_y / TILE_SIZE)}'][1] = (0, 0, 0, 0)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    canvas.draw(screen)
    pygame.display.update()

pygame.quit()
