import pygame
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 700, 500


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(
            win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y - self.VEL >= 0:
            self.y -= self.VEL

    def move_down(self):
        if self.y + self.height + self.VEL <= HEIGHT:
            self.y += self.VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y