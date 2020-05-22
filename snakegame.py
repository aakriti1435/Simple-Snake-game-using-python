import pygame
import random
import os

# os.chdir(r"C:\Users\aakriti\PycharmProjects\untitled")


pygame.mixer.init()


pygame.init()


# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (117, 217, 242)
violet = (59, 40, 96)


# Creating Window
screen_width = 800
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load("Untitled.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
bg1 = pygame.image.load("bg2.jpg")
bg1 = pygame.transform.scale(bg1,(screen_width, screen_height)).convert_alpha()
bg2 = pygame.image.load("Untitled1.png")
bg2 = pygame.transform.scale(bg2, (screen_width, screen_height)).convert_alpha()


# Game Title
pygame.display.set_caption("Snakes with Aakriti")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.blit(bgimg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        pygame.display.update()
        clock.tick(60)

# Game Loop....
def game_loop():
    # Game Specific Variables

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 3
    snake_size = 20
    fps = 60

    snk_list = []
    snk_length = 1

    if (not os.path.exists("high_scores.txt")):
        with open("high_scores.txt", "w") as f:
            f.write("0")

    with open('high_scores.txt', "r") as f:
        high_score = f.read()
        print("high_score")

    while not exit_game:
        if game_over:
            with open("high_scores.txt", "w") as f:
                f.write(str(high_score))
            gameWindow.blit(bg2, (0,0))
            text_screen("Game Over !", black, 100, 250)
            text_screen("Please Enter To Continue !", black, 100, 290)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 10
                food_x = random.randint(20, screen_width/2)
                food_y = random.randint(20, screen_height/2)
                snk_length += 3
                if score > int(high_score):
                    high_score = score

            gameWindow.blit(bg1, (0,0))
            text_screen(" Score : "+str(score), violet, 5, 5)
            text_screen(" High Score : "+str(high_score), black, 500, 550)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
