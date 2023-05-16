import pygame
from text import Text
from window import Window
from boxes import Box
from image import ImageSprite
from cannon import Cannon
from ball import Ball
from planks import Plank
from items import Items
import random


##Fruits on clouds random every time hitting objects


class Level1: 
    def __init__(self):
        self.__WINDOW = Window("Fat Bear")
    
        self.__TITLE = Text("Fat Bear")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))
        self.__TITLE.setColor((0, 0, 102))
        self.__TITLE.setFontSize(50)
        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(0)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))

        self.__BG_IMAGE = ImageSprite("images/night_bg.jpeg")
        self.__BG_IMAGE.setScale(4)
        self.__BG_IMAGE.setPosition(
            (
                0, self.__TITLE.getHeight()
            )
        )

        self.__CANNON = Cannon("images/cannon.png")
        self.__CANNON.setScale(0.2)
        self.__CANNON.setPosition((-80, 200))
        self.__CANNON.setSpeed(15)

        self.__BALLS = []
        self.NEXT_BALL = 0



############## gloria edit
        self.__ITEMS = []
        self.__ITEMS.append(Items("images/banana.png"))
        self.__ITEMS.append(Items("images/cherry.png"))
        self.__ITEMS.append(Items("images/pear.png"))
        self.__ITEMS.append(Items("images/apple.png"))
        self.__ITEMS.append(Items("images/orange.png"))
        self.__ITEMS.append(Items("images/poison.png"))
        self.__ITEMS.append(Items("images/purple_poison.png"))

        self.__ITEMS[0].setScale(0.04)
        self.__ITEMS[1].setScale(0.03)
        self.__ITEMS[2].setScale(0.04)
        self.__ITEMS[3].setScale(0.03)
        self.__ITEMS[4].setScale(0.04)
        self.__ITEMS[5].setScale(0.025)
        self.__ITEMS[6].setScale(0.053)
  
       
        self.__PLANKS = []
        for i in range(9):
            self.__PLANKS.append(Plank("images/cloud.png"))
            self.__PLANKS[i].setScale(0.07)  #plank is 0.3
            self.__PLANKS[i].setPosition((500, 0-300*i))

############### gloria edit

        


        
    

    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            KEYS_PRESSED = pygame.key.get_pressed()

            # -- PROCESSING -- #
            self.__CANNON.moveUpDown(KEYS_PRESSED)
            #self.__CANNON.checkBoundaries(-120, 800)
            
            # balls
            

            
            TIME = pygame.time.get_ticks()
            
            if KEYS_PRESSED[pygame.K_SPACE] and TIME > self.NEXT_BALL:
                DELAY = 400
                self.NEXT_BALL = TIME + DELAY
       
                BALL = Ball("images/ball.png")
                self.__BALLS.append(BALL)
                BALL.setScale(0.04)
                BALL.setPosition((self.__CANNON.getX() + 215, self.__CANNON.getY()+120))
                BALL.setSpeed(25)
                BALL.changeShoot()

            for ball in self.__BALLS:
                if ball.getShoot():
                    ball.marqueeX()
            
    
    
        
            
################ gloria edit

            # planks
            for plank in self.__PLANKS:
                plank.marqueeY(self.__WINDOW.getHeight(), 4)

            # fruits
            for item in self.__ITEMS:
                item.setPresence()
                if item.getPresence() == False:
                    item.setPosition(self.__PLANKS[0].getPOS())
            # print(self.__ITEMS[0].getPresence())
            # self.__ITEMS[0].setPosition(self.__PLANKS[0].getPOS())

            # for plank in self.__PLANKS:
            #     i = random.randrange(len(self.__ITEMS))
            #     if self.__ITEMS[i] == '':
            #         pass
            #     else:
            #         self.__ITEMS[i].setPosition(plank.getPOS())

################## gloria edit
                
       
        

    
            # -- OUTPUTS -- #
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())

            for item in self.__ITEMS:
                self.__WINDOW.getSurface().blit(item.getSurface(), item.getPOS())

            
            for plank in self.__PLANKS:
                self.__WINDOW.getSurface().blit(plank.getSurface(), plank.getPOS())

            for ball in self.__BALLS:
                self.__WINDOW.getSurface().blit(ball.getSurface(), ball.getPOS())

            
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = Level1()
    GAME.run()