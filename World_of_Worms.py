import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('World Of Worms')
 
clock = pygame.time.Clock()
 
worm_block = 10
worm_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_worm(worm_block, worm_list):
    for x in worm_list:
        pygame.draw.rect(dis, black, [x[0], x[1], worm_block, worm_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    worm_List = []
    Length_of_worm = 1
 
    foodx = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_worm - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -worm_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = worm_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -worm_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = worm_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, worm_block, worm_block])
        worm_Head = []
        worm_Head.append(x1)
        worm_Head.append(y1)
        worm_List.append(worm_Head)
        if len(worm_List) > Length_of_worm:
            del worm_List[0]
 
        for x in worm_List[:-1]:
            if x == worm_Head:
                game_close = True
 
        our_worm(worm_block,worm_List)
        Your_score(Length_of_worm - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
            Length_of_worm += 1
 
        clock.tick(worm_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()