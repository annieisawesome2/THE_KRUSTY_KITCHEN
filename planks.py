import pygame
from sprite import MySprite
from items import Items
import random

class Plank(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()


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

    
    def chooseItem(self):
        return random.choice(self.__ITEMS)
    
    def placeOnCloud(self, ITEM):
        ITEM._POS = ((self._X, self._Y - ITEM.getHeight()))


    def marqueeY(self, SCREEN_HEIGHT, SPEED):
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
            self._Y = 0 - self.getWidth()
            self._DIR_Y = 1
        if self._X == 1100 and self._Y > SCREEN_HEIGHT:
            self._X = 500
            self._Y = 0 - self.getWidth()
        self._POS = (self._X, self._Y)
  