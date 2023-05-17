
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
    
        self.__PLANKS = []
        for i in range(9):
            self.__PLANKS.append(Plank("images/cloud.png"))
            self.__PLANKS[i].setScale(0.07)  #plank is 0.3
            self.__PLANKS[i].setPosition((500, 0-300*i))


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
        

    
        self.NEXT_BALL = 0
        self.STUFF = []

    def generate(self):
        ITEM = random.choice(self.ITEMS)
        return ITEM
        
    def run(self):

        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit() 


         
             

    
            TIME = pygame.time.get_ticks()
            if TIME > self.NEXT_BALL:
                DELAY = 2000

                self.NEXT_BALL = TIME + DELAY
                ITEM = Items("images/cherry.png") #self.generate()
                self.STUFF.append(ITEM)
                ITEM.setScale(0.03)
                ITEM.setPosition((500, -5 - ITEM.getHeight()))
                ITEM.setgo()
              
            for stuff in self.STUFF:
                if ITEM.getGo:
                    stuff.marqueeY(self.__WINDOW.getHeight(), 8)
         

    
            # -- OUTPUTS -- #
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())


            for stuff in self.STUFF:
                self.__WINDOW.getSurface().blit(stuff.getSurface(), stuff.getPOS())


            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = Level1()
    GAME.run()