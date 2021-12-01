import random
import pygame

pygame.init()
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.update()

pygame.display.set_caption('Nick\'s Snake Game')

white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)


def update_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(DISPLAY, color, [x[0], x[1], snake_block, snake_block])

def check_wrap(xpos, ypos):
    if xpos == -1 * snake_block:
        xpos = DISPLAY_WIDTH - snake_block
    if xpos == DISPLAY_WIDTH:
        xpos = 0
    if ypos == -1 * snake_block:
        ypos = DISPLAY_HEIGHT - snake_block
    if ypos == DISPLAY_HEIGHT:
        ypos = 0
    return xpos, ypos

def make_food(index, food_list):
    fx = round(random.randrange(0, DISPLAY_WIDTH - snake_block) / snake_block) * snake_block
    fy = round(random.randrange(0, DISPLAY_HEIGHT - snake_block) / snake_block) * snake_block
    try:
        food_list[index] = [fx, fy]
    except IndexError:
        food_list.append([fx, fy])


def message(msg, color, height):
    message = font_style.render(msg, True, color)
    DISPLAY.blit(message, [DISPLAY_WIDTH / 3, height])


def game_loop():
    game_close = False
    game_over = False
    blue_win = False
    red_win = False
    tie = False

    x1 = y1 = DISPLAY_WIDTH / 5
    x2 = y2 = 4 * DISPLAY_WIDTH / 5
    vx1 = vy1 = vx2 = vy2 = 0

    snake_list1 = []
    snake_list2 = []
    snake_length1 = 1
    snake_length2 = 1

    food_list = []

    for index in range(10):
        make_food(index, food_list)

    while not game_over:
        while game_close == True:
            DISPLAY.fill(white)
            if blue_win:
                message("Blue wins!", red, DISPLAY_HEIGHT / 3)
                message("Press Q to quit or R to restart!", red, DISPLAY_HEIGHT / 2)
            if red_win:
                message("Red wins!", red, DISPLAY_HEIGHT / 3)
                message("Press Q to quit or R to restart!", red, DISPLAY_HEIGHT / 2)
            if tie:
                message("You tied!", red, DISPLAY_HEIGHT / 3)
                message("Press Q to quit or R to restart!", red, DISPLAY_HEIGHT / 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if vy1 == 0:
                        vy1 = snake_block
                        vx1 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if vy1 == 0:
                        vy1 = -1 * snake_block
                        vx1 = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if vx1 == 0:
                        vy1 = 0
                        vx1 = -1 * snake_block
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if vx1 == 0:
                        vy1 = 0
                        vx1 = snake_block
                if event.key == pygame.K_k:
                    if vy2 == 0:
                        vy2 = snake_block
                        vx2 = 0
                if event.key == pygame.K_i:
                    if vy2 == 0:
                        vy2 = -1 * snake_block
                        vx2 = 0
                if event.key == pygame.K_j:
                    if vx2 == 0:
                        vy2 = 0
                        vx2 = -1 * snake_block
                if event.key == pygame.K_l:
                    if vx2 == 0:
                        vy2 = 0
                        vx2 = snake_block
        x1 += vx1
        y1 += vy1
        x2 += vx2
        y2 += vy2

        x1, y1 = check_wrap(x1, y1)
        x2, y2 = check_wrap(x2, y2)

        DISPLAY.fill(white)
        update_snake(snake_block, snake_list1, blue)
        update_snake(snake_block, snake_list2, red)
        snake_head1 = [x1, y1]
        snake_head2 = [x2, y2]
        snake_list1.append(snake_head1)
        snake_list2.append(snake_head2)

        if len(snake_list1) > snake_length1:
            del snake_list1[0]
        if len(snake_list2) > snake_length2:
            del snake_list2[0]

        for snake in snake_list1[:-1]:
            if snake == snake_head2:
                blue_win = True
                game_close = True
            elif snake == snake_head1:
                red_win = True
                game_close = True

        for snake in snake_list2[:-1]:
            if snake == snake_head1:
                red_win = True
                game_close = True
            elif snake == snake_head2:
                blue_win = True
                game_close = True

        update_snake(snake_block, snake_list1, blue)
        update_snake(snake_block, snake_list2, red)

        for f in food_list:
            pygame.draw.rect(DISPLAY, green, [f[0], f[1], snake_block, snake_block])
        pygame.display.update()

        for index, f in enumerate(food_list):
            if x1 == f[0] and y1 == f[1]:
                print("blue snake ate food")
                fx = round(random.randrange(0, DISPLAY_WIDTH - snake_block) / snake_block) * snake_block
                fy = round(random.randrange(0, DISPLAY_HEIGHT - snake_block) / snake_block) * snake_block
                food_list[index] = (fx, fy)
                snake_length1 += 1
            if x2 == f[0] and y2 == f[1]:
                print("red snake ate food")
                fx = round(random.randrange(0, DISPLAY_WIDTH - snake_block) / snake_block) * snake_block
                fy = round(random.randrange(0, DISPLAY_HEIGHT - snake_block) / snake_block) * snake_block
                food_list[index] = (fx, fy)
                snake_length2 += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
