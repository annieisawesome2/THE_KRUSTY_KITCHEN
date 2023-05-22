import pygame
from sprite import MySprite
from items import Items
import random


class Plank(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.ITEM = None
        self.setScale(0.07)
        self.go = False
    
    def setgo(self):
        self.go = True
    
    def getGo(self):
        return self.go

   
        

    def addItem(self, ITEMS_LIST):
        self.ITEM = random.choice(ITEMS_LIST)

    def positionItem(self):
        self.ITEM.setPosition((self._POS))

    def marquee(self, SCREEN_HEIGHT, SPEED):
        """
        Moves object in a vertical snake pattern.
        """
        self._Y += SPEED*self._DIR_Y
        if self._X == 500 and self._Y > SCREEN_HEIGHT:
            self._X = 800
            self._Y = SCREEN_HEIGHT
            self._DIR_Y = -1

        if self._X == 800 and self._Y < 0 - self.getHeight():
            self._X = 1100
            self._Y = 0 - 20
            self._DIR_Y = 1
            
        if self._X == 1100 and self._Y > 500: #SCREEN_HEIGHT
            self.setPosition((-1000, -1000))
            
        self._POS = (self._X, self._Y)
  

