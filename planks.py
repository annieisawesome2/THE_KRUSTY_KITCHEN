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
    

    def generate(self):
        STRING = ["images/banana.png", "images/cherry.png", "images/pear.png", "images/apple.png", "images/orange.png", "images/poison.png", "images/purple_poison.png"]
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

        self.ITEM =  ITEM
        

    def addItem(self, ITEMS_LIST):
        self.ITEM = random.choice(ITEMS_LIST)

    def positionItem(self):
        self.ITEM.setPosition((self._POS))

    def marqueeY(self, SCREEN_HEIGHT, SPEED):
        """
        Moves object in a vertical snake pattern.
        """
        self._Y += SPEED*self._DIR_Y
        if self._X == 500 and self._Y > SCREEN_HEIGHT + 80:
            self._X = 800
            self._Y = SCREEN_HEIGHT + 80
            self._DIR_Y = -1
        if self._X == 800 and self._Y < 0 - self.getHeight():
            self._X = 1100
            self._Y = 0 - self.getWidth()
            self._DIR_Y = 1
        if self._X == 1100 and self._Y > 500: #SCREEN_HEIGHT
            self.setPosition((-1000, -1000))
            
        self._POS = (self._X, self._Y)
  