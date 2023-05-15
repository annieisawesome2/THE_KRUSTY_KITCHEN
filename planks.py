import pygame
from sprite import MySprite

class Plank(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()

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