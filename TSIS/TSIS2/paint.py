import pygame
import sys
from datetime import datetime
from tools import *

pygame.init()

WIDTH, HEIGHT = 1000, 700
TOPBAR = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FINAL PAINT")

canvas = pygame.Surface((WIDTH, HEIGHT - TOPBAR))
canvas.fill((255, 255, 255))

# COLORS
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

color = BLACK
brush_size = 2
tool = "pencil"

drawing = False
start_pos = None

font = pygame.font.SysFont(None, 28)
typing = False
text_input = ""
text_pos = None

clock = pygame.time.Clock()

# BUTTON CLASS
class Button:
    def __init__(self, x,y,w,h,text):
        self.rect = pygame.Rect(x,y,w,h)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen,(200,200,200),self.rect)
        txt = font.render(self.text,True,(0,0,0))
        screen.blit(txt,(self.rect.x+5,self.rect.y+5))

    def clicked(self,pos):
        return self.rect.collidepoint(pos)


# UI
tool_buttons = [
    Button(10,10,80,30,"Pencil"),
    Button(100,10,80,30,"Line"),
    Button(190,10,80,30,"Fill"),
    Button(280,10,80,30,"Text"),
]

size_buttons = [
    Button(400,10,40,30,"S"),
    Button(450,10,40,30,"M"),
    Button(500,10,40,30,"L"),
]

save_button = Button(560,10,80,30,"Save")

colors = [
    (BLACK, pygame.Rect(660,10,30,30)),
    (RED, pygame.Rect(700,10,30,30)),
    (GREEN, pygame.Rect(740,10,30,30)),
    (BLUE, pygame.Rect(780,10,30,30)),
]

while True:
    screen.fill((220,220,220))
    screen.blit(canvas,(0,TOPBAR))

    for b in tool_buttons: b.draw()
    for b in size_buttons: b.draw()
    save_button.draw()

    for col,rect in colors:
        pygame.draw.rect(screen,col,rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # KEYBOARD (Ctrl+S)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

            if typing:
                if event.key == pygame.K_RETURN:
                    img = font.render(text_input, True, color)
                    canvas.blit(img, text_pos)
                    typing = False
                    text_input = ""
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""
                else:
                    text_input += event.unicode

        # MOUSE
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos

            for i,b in enumerate(tool_buttons):
                if b.clicked((x,y)):
                    tool = ["pencil","line","fill","text"][i]

            for i,b in enumerate(size_buttons):
                if b.clicked((x,y)):
                    brush_size = [2,5,10][i]

            if save_button.clicked((x,y)):
                filename = datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)

            for col,rect in colors:
                if rect.collidepoint((x,y)):
                    color = col

            if y > TOPBAR:
                drawing = True
                start_pos = (x, y - TOPBAR)

                if tool == "fill":
                    flood_fill(canvas, start_pos[0], start_pos[1], color)

                if tool == "text":
                    typing = True
                    text_pos = start_pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if tool == "line" and start_pos:
                end = (event.pos[0], event.pos[1] - TOPBAR)
                draw_line(canvas, color, start_pos, end, brush_size)

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "pencil":
                end = (event.pos[0], event.pos[1] - TOPBAR)
                draw_pencil(canvas, color, start_pos, end, brush_size)
                start_pos = end

    # LINE PREVIEW
    if tool == "line" and drawing and start_pos:
        temp = canvas.copy()
        mx,my = pygame.mouse.get_pos()
        pygame.draw.line(temp, color, start_pos, (mx, my - TOPBAR), brush_size)
        screen.blit(temp, (0, TOPBAR))

    # TEXT PREVIEW
    if typing:
        img = font.render(text_input, True, color)
        screen.blit(img, (text_pos[0], text_pos[1] + TOPBAR))

    pygame.display.flip()
    clock.tick(60)