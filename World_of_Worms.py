import pygame
import time
import random
 
pygame.init()
black = (0, 0, 0) 
white = (255, 255, 255)
yellow = (255, 255, 102)
orange = (255, 165, 0)
red = (255, 0, 0)
green = (0, 255, 0)
leaf_green = (110, 110, 20)
blue = (0, 0, 255)
 
dis_width = 840
dis_height = 660
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('World of Worms')
icon = pygame.image.load("worm_icon.PNG")
food_image = pygame.image.load("food1.PNG")
food_image = pygame.transform.smoothscale(food_image, (25, 25))
bomb_image = pygame.image.load("bomb_worm.PNG")
bomb_image = pygame.transform.smoothscale(bomb_image, (25, 25))
gameover_image = pygame.image.load("gameover.PNG")
gameover_image = pygame.transform.smoothscale(gameover_image, (dis_width, dis_height))

pygame.display.set_icon(icon)
 
clock = pygame.time.Clock()

pos = 30
worm_block = 30
worm_speed = 8

set_caption=pygame.font.SysFont("Dilo  World",15) 
font_style = pygame.font.SysFont("Exo", 50)
score_font = pygame.font.SysFont("Exo", 15)
score_font2 = pygame.font.SysFont("Exo", 50)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score),True, white)
    dis.blit(value, [dis_width / 2.12, dis_height / 30])

def Your_score2(score):
    value = score_font2.render("Your Score: " + str(score),True, white)
    dis.blit(value, [dis_width / 2.7, dis_height / 8])
    
 
def our_worm(worm_block, worm_list):
        for x in worm_list:
            pygame.draw.rect(dis, black, [x[0], x[1], worm_block+1, worm_block+1])
            pygame.draw.rect(dis, orange, [x[0], x[1], worm_block, worm_block])
            
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 9, dis_height / 1.3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    worm_List = []
    Length_of_worm = 1

    foodx = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    foody = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    
    bombx1 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby1 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx1 == foodx and bomby1 == foody or bombx1 == x1 and bomby1 == y1:
        bombx1 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby1 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx2 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby2 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx2 == foodx and bomby2 == foody or bombx2 == x1 and bomby2 == y1:
        bombx2 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby2 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx3 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby3 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx3 == foodx and bomby3 == foody or bombx3 == x1 and bomby3 == y1:
        bombx3 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby3 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx4 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby4 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx4 == foodx and bomby4 == foody or bombx4 == x1 and bomby4 == y1:
        bombx4 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby4 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx5 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby5 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx5 == foodx and bomby5 == foody or bombx5 == x1 and bomby5 == y1:
        bombx5 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby5 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx6 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby6 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx6 == foodx and bomby6 == foody or bombx6 == x1 and bomby6 == y1:
        bombx6 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby6 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx7 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby7 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx7 == foodx and bomby7 == foody or bombx7 == x1 and bomby7 == y1:
        bombx7 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby7 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
                
    bombx8 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby8 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx8 == foodx and bomby8 == foody or bombx8 == x1 and bomby8 == y1:
        bombx8 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby8 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx9 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby9 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx9 == foodx and bomby9 == foody or bombx9 == x1 and bomby9 == y1:
        bombx9 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby9 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

    bombx10 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
    bomby10 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
    if bombx10 == foodx and bomby10 == foody or bombx10 == x1 and bomby10 == y1:
        bombx10 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
        bomby10 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
 
    while not game_over:
        
 
        while game_close == True:
            dis.fill(leaf_green)
            dis.blit(gameover_image, (0, 0))
            message("You Lost! Press C-Play Again or Q-Quit", white)
            Your_score2(Length_of_worm - 1)
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
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if(x1_change != worm_block):
                        x1_change = -worm_block
                    y1_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if(x1_change != -worm_block):
                        x1_change = worm_block
                    y1_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if(y1_change != worm_block):
                        y1_change = -worm_block
                    x1_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if(y1_change != -worm_block):
                        y1_change = worm_block
                    x1_change = 0
                    
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(leaf_green)
        dis.blit(food_image, (foodx, foody))
        dis.blit(bomb_image, (bombx1, bomby1))
        dis.blit(bomb_image, (bombx2, bomby2))
        dis.blit(bomb_image, (bombx3, bomby3))
        dis.blit(bomb_image, (bombx4, bomby4))
        dis.blit(bomb_image, (bombx5, bomby5))
        dis.blit(bomb_image, (bombx6, bomby6))
        dis.blit(bomb_image, (bombx7, bomby7))
        dis.blit(bomb_image, (bombx8, bomby8))
        dis.blit(bomb_image, (bombx9, bomby9))
        dis.blit(bomb_image, (bombx10, bomby10))
        

        worm_Head = []
        worm_Head.append(x1)
        worm_Head.append(y1)
        worm_List.append(worm_Head)
        if len(worm_List) > Length_of_worm:
            del worm_List[0]
 
        for x in worm_List[:-1]:
            if x == worm_Head:
                game_close = True
 
        our_worm(worm_block, worm_List)
        Your_score(Length_of_worm - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            foody = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            
            bombx1 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby1 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx1 == foodx and bomby1 == foody or bombx1 == x1 and bomby1 == y1:
                bombx1 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby1 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx2 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby2 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx2 == foodx and bomby2 == foody or bombx2 == x1 and bomby2 == y1:
                bombx2 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby2 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx3 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby3 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx3 == foodx and bomby3 == foody or bombx3 == x1 and bomby3 == y1:
                bombx3 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby3 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx4 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby4 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx4 == foodx and bomby4 == foody or bombx4 == x1 and bomby4 == y1:
                bombx4 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby4 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx5 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby5 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx5 == foodx and bomby5 == foody or bombx5 == x1 and bomby5 == y1:
                bombx5 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby5 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx6 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby6 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx6 == foodx and bomby6 == foody or bombx6 == x1 and bomby6 == y1:
                bombx6 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby6 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx7 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby7 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx7 == foodx and bomby7 == foody or bombx7 == x1 and bomby7 == y1:
                bombx7 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby7 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
                
            bombx8 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby8 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx8 == foodx and bomby8 == foody or bombx8 == x1 and bomby8 == y1:
                bombx8 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby8 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx9 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby9 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx9 == foodx and bomby9 == foody or bombx9 == x1 and bomby9 == y1:
                bombx9 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby9 = round(random.randrange(0, dis_height - worm_block) / pos) * pos

            bombx10 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
            bomby10 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            if bombx10 == foodx and bomby10 == foody or bombx10 == x1 and bomby10 == y1:
                bombx10 = round(random.randrange(0, dis_width - worm_block) / pos) * pos
                bomby10 = round(random.randrange(0, dis_height - worm_block) / pos) * pos
            
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
