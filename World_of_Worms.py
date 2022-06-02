import pygame
import time
import random
import os
 
pygame.init()

pygame.mixer.init()
s = 'sound'

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
btn_play = pygame.image.load("play_button.PNG")
btn_play = pygame.transform.smoothscale(btn_play, (dis_width/2, dis_height/10))
btn_instructions = pygame.image.load("instructions_button.PNG")
btn_instructions = pygame.transform.smoothscale(btn_instructions, (dis_width/1.5, dis_height/7.5))
btn_about = pygame.image.load("about_button.PNG")
btn_about = pygame.transform.smoothscale(btn_about, (dis_width/2, dis_height/10))
btn_exit = pygame.image.load("exit_button.PNG")
btn_exit = pygame.transform.smoothscale(btn_exit, (dis_width/2, dis_height/10))
logo = pygame.image.load("wow_logo.PNG")
logo = pygame.transform.smoothscale(logo, (dis_width/1.1, dis_height/2.8))
developers = pygame.image.load("developers.jpg")
developers = pygame.transform.smoothscale(developers, (dis_width, dis_height))

btn_lvl1 = pygame.image.load("level1_button.PNG")
btn_lvl1 = pygame.transform.smoothscale(btn_lvl1, (dis_width/2, dis_height/3))
btn_lvl2 = pygame.image.load("level2_button.PNG")
btn_lvl2 = pygame.transform.smoothscale(btn_lvl2, (dis_width/2, dis_height/3))
btn_lvl3 = pygame.image.load("level3_button.PNG")
btn_lvl3 = pygame.transform.smoothscale(btn_lvl3, (dis_width/2, dis_height/3))


pygame.display.set_icon(icon)
 
clock = pygame.time.Clock()

pos = 30
worm_block = 30
worm_speed = 8

set_caption=pygame.font.SysFont("Dilo  World",15) 
font_style = pygame.font.SysFont("Exo", 50)
font_style2 = pygame.font.SysFont("Exo", 40)
score_font = pygame.font.SysFont("Exo", 15)
score_font2 = pygame.font.SysFont("Exo", 50)
btn = pygame.font.SysFont("Exo", 50)
text = btn.render('quit' , True , orange) 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score),True, white)
    dis.blit(value, [dis_width / 2.12, dis_height / 30])

def Your_score2(score):
    value = score_font2.render("Your Score: " + str(score),True, white)
    dis.blit(value, [dis_width / 2.7, dis_height / 8])
    
 
def our_worm(worm_block, worm_list):
        for a in worm_list:
            pygame.draw.rect(dis, black, [a[0], a[1], worm_block+1, worm_block+1])
            pygame.draw.rect(dis, orange, [a[0], a[1], worm_block, worm_block])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4.5, dis_height / 1.35])
def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3.5, dis_height / 1.25])
def message2(msg, color):
    mesg = font_style2.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3.2, 623])

def message_ins(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 9, dis_height / 1.3])
    
def main_menu():
    class Button():
        def __init__(self, x, y, image):
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            
        def draw(self):

            action = False

            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
            
            dis.blit(self.image, (self.rect.x, self.rect.y))

            return action
            
    playButton = Button(dis_width/4, dis_height/2.27, btn_play)
    instructionsButton = Button(dis_width/6.2, dis_height/1.77, btn_instructions)
    aboutButton = Button(dis_width/4, dis_height/1.4, btn_about)
    exitButton = Button(dis_width/4, dis_height/1.2, btn_exit)

    run = True
    while run:
        dis.fill(leaf_green)

        dis.blit(logo, (dis_width/20, dis_height/25))

        if playButton.draw():
            gameLoop()
            
        if instructionsButton.draw():
            instructions()
            
        if aboutButton.draw():
            about()
            
        if exitButton.draw():
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()
    pygame.quit()
    quit()


def instructions():
    
    run1 = True
    while run1:
        dis.fill(leaf_green)

        l1 = font_style.render("Game Instructions:", True, orange)
        dis.blit(l1, [dis_width / 12, dis_height / 9])

        l2 = font_style.render("The ultimate goal of this game is for the player to achieve the highest score by not eating or hitting a bomb, the direction of the food needs to be followed by the worm. ", True, orange)
        dis.blit(l2, [dis_width / 9, dis_height / 1.3])

        l3 = font_style.render("sasa", True, orange)
        dis.blit(l3, [dis_width / 9, dis_height / 2])
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run1 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    main_menu()
                
        pygame.display.update()
    pygame.quit()
    quit()


def about():
    
    run2 = True
    while run2:
        dis.fill(leaf_green)

        dis.blit(developers,(0, 0))
        message2("Press B to Main Menu", white)
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run2 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                        main_menu()
                
        pygame.display.update()
    pygame.quit()
    quit()

 
def gameLoop():

    music1 = pygame.mixer.music.load(os.path.join(s, 'back.WAV'))
    pygame.mixer.music.play(-1)

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
            message("You Lost! Press C-Play Again", white)
            message1("B-Main Menu or Q-Quit", white)
            Your_score2(Length_of_worm - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_b:
                        main_menu()
                      
 
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
            pygame.mixer.music.stop()
            gameover_sound = pygame.mixer.Sound(os.path.join(s, 'gameover.WAV'))
            pygame.mixer.Sound.play(gameover_sound)
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
 
        for a in worm_List[:-1]:
            
            if a == worm_Head:
                pygame.mixer.music.stop()
                gameover_sound = pygame.mixer.Sound(os.path.join(s, 'gameover.WAV'))
                pygame.mixer.Sound.play(gameover_sound)
                game_close = True
 
        our_worm(worm_block, worm_List)
        Your_score(Length_of_worm - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            bite_sound = pygame.mixer.Sound(os.path.join(s, 'bite.WAV'))
            pygame.mixer.Sound.play(bite_sound)
            
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
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx2 and y1 == bomby2:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx3 and y1 == bomby3:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx4 and y1 == bomby4:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx5 and y1 == bomby5:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx6 and y1 == bomby6:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx7 and y1 == bomby7:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx8 and y1 == bomby8:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx9 and y1 == bomby9:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True

        if x1 == bombx10 and y1 == bomby10:
            pygame.mixer.music.stop()
            bomb_sound = pygame.mixer.Sound(os.path.join(s, 'bomb.WAV'))
            pygame.mixer.Sound.play(bomb_sound)
            game_close = True
 
        clock.tick(worm_speed)
 
    pygame.quit()
    quit()
 
 
main_menu()
