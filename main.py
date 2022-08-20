import pygame
import pygame, sys
from pygame.locals import *
import random
import decimal
import time
import os



    

def main():
    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()

    (width,height) = (640,640)

    DISPLAY = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Timedoom")


    bg_img1 = pygame.image.load('bg_img1.png')
    bg_img1 = pygame.transform.scale(bg_img1,(width,height))

    bg_img2 = pygame.image.load('bg_img2.png')
    bg_img2 = pygame.transform.scale(bg_img2,(width,height))
    
    bg_img3 = pygame.image.load('bg_img3.png')
    bg_img3 = pygame.transform.scale(bg_img3,(width,height))

    bg_img4 = pygame.image.load('bg_img4.png')
    bg_img4 = pygame.transform.scale(bg_img4,(width,height))

    bg_img5 = pygame.image.load('bg_img5.png')
    bg_img5 = pygame.transform.scale(bg_img5,(width,height))

    blackimage = pygame.image.load('blackpic.png')
    blackimage = pygame.transform.scale(blackimage,(width,height))

    black= (0,0,0)

    #DISPLAY.fill(black)

    TIME_TO_COMPLETE = 150
    litup = []
    pressedkeys = []

    GameState = 0

    while True:
        
        clockthing = pygame.time.get_ticks()

        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYUP:
                litup = []

            if event.type == KEYDOWN:
                litup = []
                

                pressedkey = pygame.key.name(event.key)
                pressedkey = pressedkey.replace("[","")
                pressedkey = pressedkey.replace("]","")
                print (pressedkey)
                
                try:
                    litup.append(int(pressedkey))
                    pressedkeys.append(int(pressedkey))
                except ValueError:
                    pass
            
        timetoshow = round(TIME_TO_COMPLETE - (clockthing/1000),2)

        #time complete = 200
        #time show = 190

        backgroundImage = blackimage

        #make the screen displays
        if timetoshow < (TIME_TO_COMPLETE - TIME_TO_COMPLETE * 1/5):
           backgroundImage = bg_img1
        if timetoshow < (TIME_TO_COMPLETE - TIME_TO_COMPLETE * 2/5):
            backgroundImage = bg_img2
        if timetoshow < (TIME_TO_COMPLETE - TIME_TO_COMPLETE * 3/5):
            backgroundImage = bg_img3
        if timetoshow < (TIME_TO_COMPLETE - TIME_TO_COMPLETE * 4/5):
            backgroundImage = bg_img4
        if timetoshow < (TIME_TO_COMPLETE - TIME_TO_COMPLETE * 5/5):
            backgroundImage = bg_img5

        DISPLAY.blit(backgroundImage, (0,0))
        font = pygame.font.SysFont("Arial", 50)

        levelscreen = font.render(f"TIME = {timetoshow}",True,(0,100,70))

        DISPLAY.blit(levelscreen,(width/2-150,height/2-300))

        numberlocation = {
            0:(width/2-30,height/2+100),

            1:(width/2-150,height/2-200),
            2:(width/2-30,height/2-200),
            3:(width/2+80,height/2-200),

            4:(width/2-150,height/2-100),
            5:(width/2-30,height/2-100),
            6:(width/2+80,height/2-100),

            7:(width/2-150,height/2),
            8:(width/2-30,height/2),
            9:(width/2+80,height/2),
        }

        
        listnums = [0,1,2,3,4,5,6,7,8,9]

        font2 = pygame.font.SysFont("Helvetica", 80)
        for i in listnums:
            if i in litup:
                number = font2.render(f"{i}",True,(0,200,70))
                DISPLAY.blit(number, (numberlocation[i]))

            if i not in litup:
                number = font2.render(f"{i}",True,(100,00,70))
                DISPLAY.blit(number, (numberlocation[i]))

        font3 = pygame.font.SysFont("Helvetica", 40)

        #texttalking = font3.render(f"Oh god i should call 911",True,(200,100,70))

        if GameState == 0:
            texttalking = font3.render(f"oh god the submarine is sinking",True,(100,200,70))
            texttalking2 = font3.render(f" ",True,(00,100,70))

        if "9, 1, 1" in str(pressedkeys):
            print(str(pressedkeys))
            GameState = 1
            pressedkeys = []
            texttalking = font3.render(f"Hi thank you for calling 911, please hold",True,(100,200,70))
            texttalking2 = font3.render(f"You can always press 9 to go back!",True,(00,100,70))
            TimeCalled = timetoshow
            #called at 470
            #go next at 460
        
        if GameState == 1: #OPERATORS BUSY
            if  timetoshow < TimeCalled - 8:
                texttalking = font3.render(f"Sorry ! Our operators are all currently dead",True,(100,200,70))
                texttalking2 = font3.render(f"Press 0 for BOT or 1 to hangup",True,(100,200,70))

            if "1" in str(pressedkeys):

                GameState = 0
                pressedkeys = []

            if "0" in str(pressedkeys):
                GameState = 2
                pressedkeys = []

        if GameState == 2: #TALKING TO BOT
            texttalking = font3.render(f"Thank you -or talki-g to 911-BOT",True,(100,200,70))
            texttalking2 = font3.render(f"Press 0 for Emerge-cies, 1 for Info",True,(100,200,70))
            
            if "9" in str(pressedkeys):
                GameState = 1
                pressedkeys = []

            if "1" in str(pressedkeys):
                GameState = 3
                pressedkeys = []

            if "0" in str(pressedkeys):
                GameState = 8
                pressedkeys = []

        if GameState == 3: #INFO
            #time wait maybe?
            texttalking = font3.render(f"Welcome to 911-BOT info-page",True,(100,200,70))
            texttalking2 = font3.render(f"Press 0 for your GPS, 1 for other",True,(100,200,70))
            
            if "9" in str(pressedkeys):
                GameState = 2
                pressedkeys = []

            if "1" in str(pressedkeys):
                GameState = 6
                pressedkeys = []

            if "0" in str(pressedkeys):
                GameState = 5
                pressedkeys = []

        if GameState == 5: #coordinates
            texttalking = font3.render(f"Hi these are your current-coordinates",True,(100,200,70))
            texttalking2 = font3.render(f"GPS = 3456  Press 9 to go back",True,(100,200,70))    

            if "9" in str(pressedkeys):
                GameState = 3
                pressedkeys = []       

        if GameState == 6: #other page
            texttalking = font3.render(f"Hi its been a while sin",True,(100,200,70))
            texttalking2 = font3.render(f"---ce anyone called",True,(100,200,70))    

            if "9" in str(pressedkeys):
                GameState = 3
                pressedkeys = []

            if "1" in str(pressedkeys):
                GameState = 0
                pressedkeys = []

        if GameState == 8:
            texttalking = font3.render(f"We are sorry to hear about this emergency",True,(100,200,70))
            texttalking2 = font3.render(f"Press 0 for Land-related, 1 for Naval",True,(100,200,70))

            if "9" in str(pressedkeys):
                GameState = 2
                pressedkeys = []

            if "1" in str(pressedkeys):
                GameState = 9
                pressedkeys = []

            if "0" in str(pressedkeys):
                GameState = 20
                pressedkeys = []

        if GameState == 9: #input gps

            if "9" in str(pressedkeys):
                GameState = 8
                pressedkeys = []

            if "3, 4, 5, 6" in str(pressedkeys):
                GameState = 10
                TimeCalled = timetoshow
                pressedkeys = []

            if "3456" not in str(pressedkeys):
                texttalking = font3.render(f"This bot can send help",True,(100,200,70))
                texttalking2 = font3.render(f"Please input your gps coordinates for help",True,(100,200,70))
                
                #pressedkeys = []

        if GameState == 10:
            if  timetoshow > TimeCalled - 10:
                texttalking = font3.render(f"Please hold whil------------",True,(100,200,70))
                texttalking2 = font3.render(f"We a--- sorry ab--ut your emergency",True,(100,200,70))

            if  timetoshow < TimeCalled - 10:
                texttalking = font3.render(f"You made it! Congrats",True,(100,200,70))
                texttalking2 = font3.render(f"",True,(100,200,70))

        DISPLAY.blit(texttalking, ((width/2)-300,(height/2)+200))
        DISPLAY.blit(texttalking2, ((width/2)-300,(height/2)+250))

        pygame.display.update()
    
main()