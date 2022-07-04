import pygame
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 700, 500


class Ball:
    MAX_VEL = 5
    COLOR = WHITE
    RADIUS = 7
    

    def __init__(self):
        #self.x = self.original_x = x
        #self.y = self.original_y = y
        self.x_vel = self.MAX_VEL
        self.y_vel = 0
        self.x = self.original_x = WIDTH // 2
        self.y = self.original_y = HEIGHT // 2

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.RADIUS)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel


    def handle_collision(self, left_paddle, right_paddle):
        if self.y + self.RADIUS >= HEIGHT:
            self.y_vel *= -1
        elif self.y - self.RADIUS <= 0:
            self.y_vel *= -1

        if self.x_vel < 0:
            if self.y >= left_paddle.y and self.y <= left_paddle.y + left_paddle.height:
                if self.x - self.RADIUS <= left_paddle.x + left_paddle.width:
                    self.x_vel *= -1

                    middle_y = left_paddle.y + left_paddle.height / 2
                    difference_in_y = middle_y - self.y
                    reduction_factor = (left_paddle.height / 2) / self.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.y_vel = -1 * y_vel

        else:
            if self.y >= right_paddle.y and self.y <= right_paddle.y + right_paddle.height:
                if self.x + self.RADIUS >= right_paddle.x:
                    self.x_vel *= -1

                    middle_y = right_paddle.y + right_paddle.height / 2
                    difference_in_y = middle_y - self.y
                    reduction_factor = (right_paddle.height / 2) / self.MAX_VEL
                    y_vel = difference_in_y / reduction_factor
                    self.y_vel = -1 * y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1