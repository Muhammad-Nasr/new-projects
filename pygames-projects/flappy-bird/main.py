from asyncio.events import BaseDefaultEventLoopPolicy
import pygame
import sys
import random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 650))  # y position to start from 
    screen.blit(floor_surface, (floor_x_pos + 576, 650))

# a function to create pipe
# get_rect (surface_name, ( x position to start from, y position to start form))
def create_pipe():
    random_x_pos_top = random.choice(pipe_x_pos_list)
    random_x_pos_bottom = random.choice(pipe_x_pos_list)
    random_y_pos = random.choice(pipe_y_pos_list)
    bottom_pipe = pipe_surface.get_rect(midtop=(random_x_pos_bottom, random_y_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(random_x_pos_top, random_y_pos - 400))
    return bottom_pipe, top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5   
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:
            screen.blit(pipe_surface, pipe)
        else:
            # flip (surface, bool(flip-x), bool(flip-y) )
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)    

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 800:
        death_sound.play()
        return False
    
    return True

def rotate_bird(bird):
    rotated_bird = pygame.transform.rotozoom(bird, bird_movement * 3, 1)
    return rotated_bird

def bird_animation():
    new_bird_surface = bird_frames[bird_index]
    new_bird_rect = new_bird_surface.get_rect(center=(100, bird_rect.centery))

    return new_bird_surface, new_bird_rect

def score_display(game_over=False):
  
    score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
    score_rect = score_surface.get_rect(center=(288, 50))
    screen.blit(score_surface, score_rect)

    if game_over:
        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(288, 630))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score




pygame.init()

## game variables
gravity = 0.25
bird_movement = 0 
game_active = True
score = 0
high_score = 0

screen = pygame.display.set_mode((576, 900))  ## (w, h)
# limit frame per second
clock = pygame.time.Clock()
# create font
game_font = pygame.font.Font('assets/04B_19.TTF', 40)

# load the bg image
bg_surface = pygame.image.load('assets/background-day.png').convert() # cnovert image to a file
bg_surface = pygame.transform.scale2x(bg_surface)   # scale the image 2 time = all the screen

# load base image
floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0   ## position to start from x in the screen
 
 # load birds
## create three birds, make animation

bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png').convert_alpha()) 
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert_alpha()) 
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png').convert_alpha()) 
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100, 300))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

## create one bird
# bird_surface = pygame.image.load('assets/bluebird-midflap.png')
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center=(100, 300))


# create pipes ------------------------------------------------ 
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()

#pipe_surface = pygame.transform.scale2x(pipe_surface)

SPANPIPE = pygame.USEREVENT
pygame.time.set_timer(SPANPIPE, 1200)
pipe_list = []
pipe_y_pos_list = [500, 550, 450]
pipe_x_pos_list = [600, 700, 800]

# game-over load
game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha()) 
game_over_rect = game_over_surface.get_rect(center=(288, 340))

# create sound play

flap_sound = pygame.mixer.Sound('sound/sfx_wing.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')
score_sound_countdown = 100
SCOREEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCOREEVENT,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = -10
                flap_sound.play()

            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 200)
                bird_movement = 0
                score = 0         
        
        if event.type == SPANPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

            bird_surface, bird_rect = bird_animation()
            
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # bird
        rotated_bird = rotate_bird(bird=bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipes=pipe_list)
        bird_movement += gravity
        
        # pipes
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        # score
        score += 0.1
        score_sound_countdown -= 1
        score_display()
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100

    else:
        high_score = update_score(score, high_score)
        score_display(game_over=True)
        screen.blit(game_over_surface, game_over_rect)
        
        
    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos == -576:
        floor_x_pos = 0

    
    pygame.display.update()
    clock.tick(120)

