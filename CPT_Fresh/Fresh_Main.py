# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu

import pygame
import random
import math
import os
#os.environ['SDL_VIDEODRIVER']='windib'
from wall import *
from platform import *
from block import *
from player import *

#-------------------------------------------------------------------------------

pygame.init()

# Set the height and width of the screen
size=[800,600]
screen=pygame.display.set_mode(size)

#Load all images
greenB = pygame.image.load("green.png").convert()
yellowB = pygame.image.load("yellow.png").convert()
redB = pygame.image.load("red.png").convert()
orangeB = pygame.image.load("orange.png").convert()
carelton = pygame.image.load("carelton.png").convert()
rain = pygame.image.load("RainbowBridge.png").convert()
mountain = pygame.image.load("mountain.png").convert()
bboard = pygame.image.load("bboard.png").convert()
blueB = pygame.image.load("blueB.png").convert()
purpleB = pygame.image.load("purpleB.png").convert()
pygame.display.set_caption("Fresh!")


#-------------------------------------------------------------------------------

"""Create object instances of blocks which act as pipes to each level"""
def menu():
    block_list = pygame.sprite.RenderPlain()
    infoBlock = Block("InfoPipe.png")
    infoBlock.rect.x = 350
    infoBlock.rect.y = 132
    block_list.add(infoBlock)

    highBlock = Block("HighPipe.png")
    highBlock.rect.x = 500
    highBlock.rect.y = 132
    block_list.add(highBlock)

    quitBlock = Block("QuitPipe.png")
    quitBlock.rect.x = 650
    quitBlock.rect.y = 132
    block_list.add(quitBlock)

    playBlock = Block("PlayPipe.png")
    playBlock.rect.x = 200
    playBlock.rect.y = 132
    block_list.add(playBlock)


    MenuBlock = Block("MenuTitle.png")
    MenuBlock.rect.x = 15
    MenuBlock.rect.y = 15
    block_list.add(MenuBlock)


    walls = [[0,15,15,600,green],[785,15,15,600,green],[0,0,800,15,green],[15,585,800,15,green],[0,127,900,15,green]]
    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    return block_list

#------------------------------------------------------------------------------------------------

#info room
def info():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    return block_list

#highscore room
def high():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    return block_list


#------------------------------------------------------------------------------------------------

#Defining ALL LEVELS

def level1():

    block_list = pygame.sprite.RenderPlain()

    #First 4 are walls, rest are platforms
    walls = [[0,15,15,600,white],
            [785,15,15,600,white],
            [0,0,800,15,white],
            [15,585,800,15,white],
            [80,520,70,10,white],
            [160,460,70,10,white],
            [250,250,10,500,white],[50,390,70,10,white],[160,320,70,10,white],
            [330,240,70,10,white],[450,170,70,10,white],[600,130,10,700,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list


def level2():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],
            [785,15,15,600,white],
            [0,0,800,15,white],
            [15,585,800,15,white],
            [150,200,15,400,orange],
            [150,200,500,15,orange],
            [20,500,30,10,orange],
            [115,425,30,10,orange],
            [20,350,30,10,orange],
            [115,275,30,10,orange],
            [20,200,30,10,orange],
            [150,140,15,60,orange],
            [115,275,30,10,orange],
            [300,150,30,10,orange],
            [450,125,30,10,orange],
            [635,100,15,100,orange],
            [745,130,30,10,orange],
            [650,205,30,10,orange],
            [250,300,535,100,orange],
            [300,535,15,50,orange],
            [615,535,15,50,orange]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list

def level3():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white],
    [700,150,10,700,white],[0,510,625,10,white],[100,435,600,10,white],[0,360,100,10,white],[200,360,425,10,white],
    [350,360,10,75,white],[0,290,200,10,white],[300,290,400,10,white],[0,220,100,10,white],[200,220,425,10,white],
    [0,150,200,10,white],[300,150,280,10,white],[650,150,55,10,white],[0,80,800,10,white],[550,80,10,75,white],
    [470,150,10,75,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list

def level4():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white],[650,130,10,700,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    y = 520
    for i in range(6):
        for j in range(3):
            x = random.randint(80,600)
            wall = Wall(x,y,40,10,rBlue)
            block_list.add(wall)
        y = y - 70


    y = 470
    for i in range(6):
        for j in range(3):
            x = random.randint(80,600)
            wall = Wall(x,y,10,60,rBlue)
            block_list.add(wall)
        y = y - 70


    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list

def level5():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white],
    [15,75,100,10,white],[700,100,10,600,white],[50,475,10,10,white],[200,15,10,300,white],
    [250,400,10,10,white],[450,400,10,10,white],[680,350,10,10,white],[500,275,10,10,white],
    [290,200,10,10,white],[200,150,30,10,white],[400,100,300,10,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list

def level6():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,green],
            [785,15,15,600,white],
            [0,0,800,15,white],
            [15,585,800,15,white],
            [100,515,10,10,white],
            [30,435,10,10,white],
            [150,0,15,275,white],
            [150,400,15,300,white],
            [250,0,15,225,white],
            [250,325,15,275,white],
            [350,0,15,280,white],
            [350,355,15,300,white],
            [450,0,15,380,white],
            [450,450,15,150,white],
            [625,425,10,10,white],
            [475,375,10,10,white],
            [550,500,10,10,white],
            [610,290,10,10,white],
            [550,210,10,10,white],
            [650,0,15,100,white],
            [650,155,15,445,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list

def level7():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white],[700,50,10,200,white],
    [700,325,10,350,white],[600,550,100,10,white],[500,470,10,10,white],[300,420,10,10,white],[50,370,10,10,white],
    [275,300,10,10,white],[50,230,10,10,white],[275,160,10,10,white],[475,90,10,10,white],[550,150,150,10,white],
    [620,325,10,10,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    paintBlock = Block("freshPaint.png")
    paintBlock.rect.x = 735
    paintBlock.rect.y = 515
    block_list.add(paintBlock)

    return block_list

def completeLevel():

    block_list = pygame.sprite.RenderPlain()

    walls = [[0,15,15,600,white],[785,15,15,600,white],[0,0,800,15,white],[15,585,800,15,white]]

    for item in walls:
        wall=Wall(item[0],item[1],item[2],item[3],item[4])
        block_list.add(wall)

    return block_list



#-------------------------------------------------------------------------------



def main():
    try:
        moving_sprites_list = pygame.sprite.RenderPlain()
        change = 0
        player = Player(20, 15)

        player.rect.x = 20
        player.rect.y = 450

        moving_sprites_list.add(player)

        #set current room to menu
        currentRoom = 0
        block_list = menu()

        font = pygame.font.Font(None, 36)
        time = 250

        #Loop until the user clicks the close button.
        done=False

        # Used to manage how fast the screen updates
        clock=pygame.time.Clock()

        #load all sounds
        song = pygame.mixer.Sound("bel_air.wav")
        song.play()
        jumpSound = pygame.mixer.Sound("smb_jump-super.wav")
        coinSound = pygame.mixer.Sound("smb_coin.wav")
        completeSound = pygame.mixer.Sound("smb_stage_clear.wav")
        tomjones = pygame.mixer.Sound("tomjones.wav")
        bwong = pygame.mixer.Sound("bwong.wav")

        # -------- Main Program Loop -----------
        while done==False:

            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.changespeed_x(-6)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed_x(6)
                    if event.key == pygame.K_UP:
                        player.jump(block_list)
                        jumpSound.play()
                    if event.key == pygame.K_DOWN:
                        player.changespeed_y(6)

                    #bring them back to menu
                    if event.key == pygame.K_m:
                        currentRoom = 0
                        block_list = menu()
                        player.rect.x = 20
                        player.rect.y = 500
                        time = 250

                    #reset player to start of level
                    if event.key == pygame.K_r:
                        if currentRoom == 7:
                            player.rect.x = 20
                            player.rect.y = 20
                        else:
                            player.rect.x = 20
                            player.rect.y = 450

                    #randomize layout of level 4
                    if event.key == pygame.K_n and currentRoom == 6:
                        block_list = level4()
                        player.rect.x = 20

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.changespeed_x(-0)
                    if event.key == pygame.K_RIGHT:
                        player.changespeed_x(0)


            player.calc_grav()
            player.update(block_list)
            block_list.update()

        #----------------------------------------------------------------------------------------------------------
        #ROOM CONDITIONS

            #If user selects to play, go to level 1
            if player.rect.x > 200 and player.rect.x < 230 and player.rect.y < 483.5 and currentRoom == 0:
                block_list = level1()
                currentRoom = 3
                player.rect.x = 20
                player.rect.y = 525

            #If user selects info, go to info screen
            if player.rect.x > 350 and player.rect.x < 380 and player.rect.y < 483.5 and currentRoom == 0:
                block_list = info()
                currentRoom = 1
                player.rect.x = 20
                player.rect.y = 525

            #If user selects high, go to high screen
            if player.rect.x > 500 and player.rect.x < 530 and player.rect.y < 483.5 and currentRoom == 0:
                block_list = info()
                currentRoom = 2
                player.rect.x = 20
                player.rect.y = 525

            #if user is in info screen, let them go back to menu
            if player.rect.x > 700 and currentRoom == 1:
                currentRoom = 0
                block_list = menu()
                player.rect.x = 20

            #if user is in high screen, let them go back to menu
            if player.rect.x > 700 and currentRoom == 2:
                currentRoom = 0
                block_list = menu()
                player.rect.x = 20

            #If user selects quit, quit the program
            if player.rect.x > 650 and player.rect.x < 680 and player.rect.y < 484 and currentRoom == 0:
                pygame.quit ()


        #---------------------------------------------------------------------------------------------------------
        #LEVEL CONDITIONS/SWITCHING

            #If user completes level 1, go to level 2
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 3:
                coinSound.play()
                block_list = level2()
                currentRoom = 4
                player.rect.x = 20
                player.rect.y = 525

            #If user completes level 2, go to level 3
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 4:
                coinSound.play()
                block_list = level3()
                currentRoom = 5
                player.rect.x = 20
                player.rect.y = 525

            #If user completes level 3, go to level 4
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 5:
                coinSound.play()
                block_list = level4()
                currentRoom = 6
                player.rect.x = 20
                player.rect.y = 525


            #If user completes level 4, go to level 5
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 6:
                coinSound.play()
                block_list = level5()
                currentRoom = 7
                player.rect.x = 20
                player.rect.y = 20

            #If user completes level 5, go to level 6
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 7:
                coinSound.play()
                block_list = level6()
                currentRoom = 8
                player.rect.x = 20
                player.rect.y = 525

            #If user completes level 6, go to level 7
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 8:
                song.stop()
                bwong.play()
                block_list = level7()
                currentRoom = 9
                player.rect.x = 20
                player.rect.y = 525
                tomjones.play()

            #If user completes level 7, go to complete room
            if player.rect.x > 679 and player.rect.y >459 and currentRoom == 9:
                completeSound.play()
                block_list = completeLevel()
                currentRoom = 10
                player.rect.x = 20

            if time <= 0:
                block_list = menu()
                currentRoom = 0
                player.rect.x = 20
                time = 250
        #---------------------------------------------------------------------------------------------------------
        #DRAW EVERYTHING BASED ON THE CONDITIONS

            #starts the timer
            if currentRoom > 2 and currentRoom < 10:
                time = time - 0.023

            # Set the screen background
            screen.fill(black)

            if currentRoom == 1:
                screen.blit(bboard, [0,15])

            if currentRoom == 2:
                screen.blit(mountain, [0,0])

            if currentRoom == 3:
                screen.blit(redB, [0,0])

            if currentRoom == 4:
                screen.blit(orangeB, [0,0])

            if currentRoom == 5:
                screen.blit(yellowB, [0,0])

            if currentRoom == 6:
                screen.blit(greenB, [0,0])

            if currentRoom == 7:
                screen.blit(blueB, [0,0])

            if currentRoom == 8:
                screen.blit(purpleB, [0,0])

            if currentRoom == 9:
                screen.blit(carelton,[0,0])

            if currentRoom == 10:
                screen.blit(rain, [0,0])

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            block_list.draw(screen)
            moving_sprites_list.draw(screen)

            #draw the time/score
            try:
                text=font.render("Time: "+str(time), True, white)
                screen.blit(text, [650, 20])
            except:
                pass

            #draw the level #
            if currentRoom > 2 and currentRoom < 10:
                try:
                    text1=font.render("Level #" + str(currentRoom - 2), True, white)
                    screen.blit(text1, [50, 20])
                except:
                    pass

            #draw the menu instruction
            if currentRoom > 0:
                try:
                    text1=font.render("Menu [m]", True, white)
                    screen.blit(text1, [240, 20])
                except:
                    pass

            #draw the reset instruction
            if currentRoom > 2:
                try:
                    text1=font.render("Reset [r]", True, white)
                    screen.blit(text1, [430, 20])
                except:
                    pass


            #If user selects info, display instructions, etc from a text file
            if currentRoom == 1:
                try:
                    text1=font.render("Use the arrow keys to move left and right and to jump", True, white)
                    text2=font.render("Procede through each level collecting paintcans in 250s", True, white)
                    text3=font.render("Hints at the top screen and prepare for Carelton!", True, white)
                    screen.blit(text3, [100, 400])
                    screen.blit(text1, [100, 200])
                    screen.blit(text2, [100, 300])
                except:
                    pass

            hiscore = open("highscore.txt","r")
            leader  = hiscore.read()
            hiscore.close

            #If user selects high, display highscore
            if currentRoom == 2:
                try:
                    text1=font.render("The best time is: "+ str(leader), True, white)
                    screen.blit(text1, [100, 250])
                except:
                    pass

            #If user is in info/highscore
            if currentRoom == 2 or currentRoom == 1:
                try:
                    text1=font.render("Menu -->", True, white)
                    screen.blit(text1, [670, 500])
                except:
                    pass

            #If user is in info/highscore
            if currentRoom == 3:
                try:
                    text1=font.render("Press R to reset", True, white)
                    screen.blit(text1, [350, 550])
                except:
                    pass

            #If user is in info/highscore
            if currentRoom == 6:
                try:
                    text1=font.render("Press N for new layout", True, white)
                    screen.blit(text1, [50, 50])
                except:
                    pass


            #If user finishes all levels, congrats!
            if currentRoom == 10:
                try:
                    text1=font.render("Thank you Fresh for Restoring the colour to Bel Air", True, white)
                    text3=font.render("An end to Bruno & Amro's ICS2O/3U/4U career.", True, white)
                    text2=font.render("Press the M key to return to the Menu", True, white)
                    screen.blit(text1, [100, 350])
                    screen.blit(text3, [100, 390])
                    screen.blit(text2, [100, 430])
                except:
                    pass

            #write new highscore if users is better than old one
            if currentRoom == 10:
                if str(time) >= leader:
                    try:
                        text4=font.render("Congratulations, you got the best time!", True, white)
                        screen.blit(text4, [100, 470])
                        hiscore = open("highscore.txt","w")
                        hiscore.write(str(time))
                        hiscore.close
                    except:
                        pass

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            # Limit to 20 frames per second
            clock.tick(40)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit ()
    except:
        print ("Thanks for playing!")
main()


