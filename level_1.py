
import pygame
from text import Text
from window import Window
from boxes import Box
from image import ImageSprite
from cannon import Cannon
from ball import Ball
from planks import Plank
from items import Items
from bear import Bear
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

        self.__BEAR = Bear("images/panda_bear.png")
        self.__BEAR.setPosition((1050, 650))
        self.__BEAR.setScale(0.5)
        



############## gloria edit
    
        self.__PLANKS = []
        for i in range(9):
            self.__PLANKS.append(Plank("images/cloud.png"))
            self.__PLANKS[i].setScale(0.07)  #plank is 0.3
            self.__PLANKS[i].setPosition((500, 0-300*i))

############### gloria edit

        self.ITEMS = [
                Items("images/banana.png"),
                Items("images/cherry.png"),
                Items("images/pear.png"),
                Items("images/apple.png"),
                Items("images/orange.png"),
                Items("images/poison.png"),
                Items("images/purple_poison.png")
            ]

        self.ITEMS[0].setScale(0.04)
        self.ITEMS[1].setScale(0.03)
        self.ITEMS[2].setScale(0.04)
        self.ITEMS[3].setScale(0.03)
        self.ITEMS[4].setScale(0.04)
        self.ITEMS[5].setScale(0.025)
        self.ITEMS[6].setScale(0.053)

        
        

        #self.RANDOM_ITEM1 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM2 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM3 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM4 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM5 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM6 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM7 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM8 = self.ITEMS[random.randint(0,6)]
        #self.RANDOM_ITEM9 = self.ITEMS[random.randint(0,6)]


    

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

            # planks
            for plank in self.__PLANKS:
                plank.marqueeY(self.__WINDOW.getHeight(), 8)
            
        
     
            #self.RANDOM_ITEM1.setPosition((self.__PLANKS[0]._POS))
            #self.RANDOM_ITEM2.setPosition((self.__PLANKS[1]._POS))
            #self.RANDOM_ITEM3.setPosition((self.__PLANKS[2]._POS))
            #self.RANDOM_ITEM4.setPosition((self.__PLANKS[3]._POS))
            #self.RANDOM_ITEM5.setPosition((self.__PLANKS[4]._POS))
            #self.RANDOM_ITEM6.setPosition((self.__PLANKS[5]._POS))
            #self.RANDOM_ITEM7.setPosition((self.__PLANKS[6]._POS))
            #self.RANDOM_ITEM8.setPosition((self.__PLANKS[7]._POS))
            #self.RANDOM_ITEM9.setPosition((self.__PLANKS[8]._POS))

        
            
################ gloria edit
            '''
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
            '''
            # -- OUTPUTS -- #
           
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())

    


            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())

            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM1.getSurface(), self.RANDOM_ITEM1.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM2.getSurface(), self.RANDOM_ITEM2.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM3.getSurface(), self.RANDOM_ITEM3.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM4.getSurface(), self.RANDOM_ITEM4.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM5.getSurface(), self.RANDOM_ITEM5.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM6.getSurface(), self.RANDOM_ITEM6.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM7.getSurface(), self.RANDOM_ITEM7.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM8.getSurface(), self.RANDOM_ITEM8.getPOS())
            #self.__WINDOW.getSurface().blit(self.RANDOM_ITEM9.getSurface(), self.RANDOM_ITEM9.getPOS())

            
            for plank in self.__PLANKS:
                self.__WINDOW.getSurface().blit(plank.getSurface(), plank.getPOS())

            

            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())

            


            
            for ball in self.__BALLS:
                self.__WINDOW.getSurface().blit(ball.getSurface(), ball.getPOS())
            
            self.__WINDOW.getSurface().blit(self.__BEAR.getSurface(),self.__BEAR.getPOS())

            
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = Level1()
    GAME.run()