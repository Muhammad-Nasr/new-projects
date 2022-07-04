import os
import pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))


# title and icon
pygame.display.set_caption('Space Invadors')
sourceFileDir = os.path.dirname(os.path.abspath(__file__))

iconPath = os.path.join(sourceFileDir, 'rocky.png')
icon = pygame.image.load(iconPath) 
pygame.display.set_icon(icon)



# create game loop 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 0, 0))
    pygame.display.update()

pygame.quit()


