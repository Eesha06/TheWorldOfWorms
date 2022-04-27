import pygame
import time
import random
 
pygame.init()
black = (0, 0, 0) 
white = (255, 255, 255)
yellow = (255, 255, 102)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('World of Worms')
 
clock = pygame.time.Clock()
 
worm_block = 10
worm_speed = 15

set_caption=pygame.font.SysFont("Dilo  World",15) 
font_style = pygame.font.SysFont("Exo", 30)
score_font = pygame.font.SysFont("Exo", 15)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score),True, white)
    dis.blit(value, [dis_width / 2.5, dis_height / 30])
 
def our_worm(worm_block, worm_list):
        for x in snake_list:
            pygame.draw.rect(dis, green, [x[0], x[1], worm_block, worm_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 2])
 
 
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

    bombx1 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby1 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
    
    bombx2 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby2 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx3 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby3 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx4 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby4 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx5 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby5 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx6 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby6 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx7 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby7 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx8 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby8 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx9 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby9 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

    bombx10 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
    bomby10 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
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
                if event.key == pygame.K_a:
                    if(x1_change != worm_block):
                        x1_change = -worm_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    if(x1_change != -worm_block):
                        x1_change = worm_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    if(y1_change != worm_block):
                        y1_change = -worm_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    if(y1_change != -worm_block):
                        y1_change = worm_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx, foody, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx1, bomby1, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx2, bomby2, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx3, bomby3, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx4, bomby4, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx5, bomby5, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx6, bomby6, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx7, bomby7, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx8, bomby8, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx9, bomby9, worm_block, worm_block])
        pygame.draw.rect(dis, red, [bombx10, bomby10, worm_block, worm_block])

        worm_Head = []
        worm_Head.append(x1)
        worm_Head.append(y1)
        worme_List.append(worm_Head)
        if len(worm_List) > Length_of_worm:
            del worm_List[0]
 
        for x in worm_List[:-1]:
            if x == worm_Head:
                game_close = True
 
        our_snake(worm_block, worm_List)
        Your_score(Length_of_worm - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx1 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby1 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx2 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby2 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx3 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby3 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx4 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby4 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx5 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby5 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx6 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby6 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx7 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby7 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx8 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby8 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx9 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby9 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0

            bombx10 = round(random.randrange(0, dis_width - worm_block) / 10.0) * 10.0
            bomby10 = round(random.randrange(0, dis_height - worm_block) / 10.0) * 10.0
            Length_of_worm += 1

        if x1 == bombx1 and y1 == bomby1:
            game_close = True

        if x1 == bombx2 and y1 == bomby2:
            game_close = True

        if x1 == bombx3 and y1 == bomby3:
            game_close = True

        if x1 == bombx4 and y1 == bomby4:
            game_close = True

        if x1 == bombx5 and y1 == bomby5:
            game_close = True

        if x1 == bombx6 and y1 == bomby6:
            game_close = True

        if x1 == bombx7 and y1 == bomby7:
            game_close = True

        if x1 == bombx8 and y1 == bomby8:
            game_close = True

        if x1 == bombx9 and y1 == bomby9:
            game_close = True

        if x1 == bombx10 and y1 == bomby10:
            game_close = True
 
        clock.tick(worm_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
