

import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height)) # Size of window

# Game Title
pygame.display.set_caption("My First Game - Snake Game")
pygame.display.update()
clock = pygame.time.Clock() # Clock() is used to create clock object to help track time
font = pygame.font.SysFont(None, 55) #create a Font object from the system fonts

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color) #render()-draw text on a new Surface
    gameWindow.blit(screen_text, [x,y])   #blit-to update the screen


def plot_snake(gameWindow, color, snk_list, snake_size):    # To draw the increasing length of snake size
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 45

    with open("hiscore.txt","r") as f:
        hiscore=f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():    #For exiting to click cross button of window frame
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():           #For exiting to click cross button of window frame
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:  #moving snake right for pressing the right arrow key
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:        #moving snake left for pressing the left arrow key
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:       #moving snake up for pressing the up arrow key
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:    #moving snake down for pressing the down arrow key
                        velocity_y = init_velocity
                        velocity_x = 0



            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:  #conditoon for eating food
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=3

                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("Score: " + str(score) +"                                                   "+ "HiScore: "+ str(hiscore), red, 5, 5)  #Display Score on the window
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []           # to start the snake
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:   # for coliding at any end of the window then game is over
                game_over = True
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()



#FPS constitutes as to how many frames (images)  monitor is displaying each second