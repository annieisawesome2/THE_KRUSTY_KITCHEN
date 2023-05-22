
import pygame
from text import Text
from window import Window
from boxes import Box
from image import ImageSprite
from cannon import Cannon
from ball import Ball
from planks import Plank
from items import Items
from bucket import Bucket
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
        self.__BG_IMAGE.setPosition((0, self.__TITLE.getHeight()))

        self.__CANNON = Cannon("images/cannon.png")
        self.__CANNON.setScale(0.16)
        self.__CANNON.setPosition((-60, 200))
        self.__CANNON.setSpeed(15)

        self.__BALLS = []
    
        self.NEXT_BALL = 0

        self.__BUCKET = Bucket("images/bucket.png")
        self.__BUCKET.setPosition((1085, 530))
        self.__BUCKET.setScale(0.2)
        self.__FRONT_BUCKET = Bucket("images/bucket2.png")
        self.__FRONT_BUCKET.setPosition((1085, 585))
        self.__FRONT_BUCKET.setScale(0.2)

        self.POINTS = 0
        self.HEALTH_BAR = []
        for i in range(15):
            self.HEALTH_BAR.append(Box(15, 10))
            self.HEALTH_BAR[i].setPosition((1075+i*12, 535+self.__BUCKET.getHeight()))
        
        self.__PLANKS = [Plank("images/cloud.png")]
        self.__PLANKS[0].setPosition((500, 0-self.__PLANKS[0].getHeight()))
        self.NEXT_PLANK = 0
        
        self.NEXT_ITEM = 0
        self.STUFF = []

    def generate(self):
        STRING = ["images/banana.png", "images/cherry.png", "images/pear.png", "images/apple.png", "images/orange.png", "images/poison.png", "images/purple_poison.png", "images/poison.png", "images/purple_poison.png"]
        CHOSEN_ITEM = random.choice(STRING)

        ITEM = Items(CHOSEN_ITEM)

        if CHOSEN_ITEM == "images/banana.png":
            ITEM.setScale(0.04)
        elif CHOSEN_ITEM == "images/cherry.png":
            ITEM.setScale(0.03)
        elif CHOSEN_ITEM == "images/pear.png":
            ITEM.setScale(0.04)
        elif CHOSEN_ITEM == "images/apple.png":
            ITEM.setScale(0.03)
        elif CHOSEN_ITEM == "images/orange.png":
            ITEM.setScale(0.04)
        elif CHOSEN_ITEM == "images/poison.png":
            ITEM.setScale(0.025)
        elif CHOSEN_ITEM == "images/purple_poison.png":
            ITEM.setScale(0.053)

        return ITEM
        

    
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

            self.__CANNON.checkBoundaries(0, 820)
            
            # balls
            TIME1 = pygame.time.get_ticks()
            
            if KEYS_PRESSED[pygame.K_SPACE] and TIME1 > self.NEXT_BALL:
                DELAY_1 = 400
                self.NEXT_BALL = TIME1 + DELAY_1
       
                BALL = Ball("images/ball.png")
               

                self.__BALLS.append(BALL)
                BALL.setScale(0.03)
                BALL.setPosition((self.__CANNON.getX() + 160, self.__CANNON.getY()+100))
                BALL.setSpeed(25)
                BALL.changeShoot()

            for ball in self.__BALLS:
                if ball.getShoot():
                    ball.marqueeX()
                if ball.getPOS()[0] > self.__WINDOW.getWidth():
                    self.__BALLS.pop(0)
                    del ball

            #-----collisions ----------------
            for ball in self.__BALLS:
                for stuff in self.STUFF:
                    BALL_MASK = pygame.mask.from_surface(ball.getSurface())
                    ITEM_MASK = pygame.mask.from_surface(stuff.getSurface())
                    if BALL_MASK.overlap(ITEM_MASK, ((stuff._X - ball._X, stuff._Y - ball._Y))):
                        ball.setPosition((-1000,-1000))
                        self.__BALLS.pop(self.__BALLS.index(ball))
                        stuff.setPosition((-1000,-1000))
                        self.STUFF.pop(self.STUFF.index(stuff))
            
      
# planks -------------------------------------------------------------------------------------------
            # # planks
            # PLANK_TIME = pygame.time.get_ticks()
            # if PLANK_TIME > self.NEXT_PLANK:
            #     DELAY = 2000
            #     self.NEXT_PLANK = PLANK_TIME + DELAY
            #     PLANK = Plank("images/cloud.png")
            #     self.__PLANKS.append(PLANK)
            #     PLANK.setPosition((500, 0 - self.__PLANKS[-1].getHeight()))

            # for plank in self.__PLANKS:
            #     plank.marqueeY(self.__WINDOW.getHeight(), 8)
            #     if plank.getPOS() == [1100, self.__WINDOW.getHeight() + plank.getHeight()]:
            #         self.__PLANKS.pop(0)
            #         del plank
# ---------------------------------------------------------------------------------------------------
     
    
            #items
            TIME = pygame.time.get_ticks()
            if TIME > self.NEXT_ITEM:
                DELAY = 1500

                self.NEXT_ITEM = TIME + DELAY
                ITEM = self.generate()
                self.STUFF.append(ITEM)
                #ITEM.setScale(0.03)
                ITEM.setPosition((500, -5 - ITEM.getHeight()))
                ITEM.setgo()
              
            for stuff in self.STUFF:
                if ITEM.getGo:
                    stuff.marqueeY(self.__WINDOW.getHeight(), 12)
                    
                # points
                if stuff.getCollected():
                    if stuff.getFileLoc() != "images/purple_poison.png" and stuff.getFileLoc() != "images/poison.png":
                        self.POINTS += 1
                    elif stuff.getFileLoc() == "images/poison.png":
                        self.POINTS -= 1
                    elif stuff.getFileLoc() == "images/purple_poison.png":
                        self.POINTS -= 3
                    self.STUFF.pop(self.STUFF.index(stuff))
                    del stuff
            print(self.POINTS)

   
            # -- OUTPUTS -- #
                
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
       
            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())

            self.__WINDOW.getSurface().blit(self.__BUCKET.getSurface(), self.__BUCKET.getPOS())
           
            # for plank in self.__PLANKS:
            #     self.__WINDOW.getSurface().blit(plank.getSurface(), plank.getPOS())

            for stuff in self.STUFF:
                self.__WINDOW.getSurface().blit(stuff.getSurface(), stuff.getPOS())

            for ball in self.__BALLS:
                self.__WINDOW.getSurface().blit(ball.getSurface(), ball.getPOS())
            

            # self.__WINDOW.getSurface().blit(self.__BEAR.getSurface(),self.__BEAR.getPOS()
            self.__WINDOW.getSurface().blit(self.__FRONT_BUCKET.getSurface(), self.__FRONT_BUCKET.getPOS())

            for interval in self.HEALTH_BAR:
                self.__WINDOW.getSurface().blit(interval.getSurface(), interval.getPOS())

            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = Level1()
    GAME.run()