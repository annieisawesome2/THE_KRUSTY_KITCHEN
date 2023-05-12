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
        self._Y += SPEED
        if self._X == 500 and self._Y > SCREEN_HEIGHT:
            self._X = 800
            self._Y = 0 - self.getWidth()
        if self._X == 800 and self._Y > SCREEN_HEIGHT:
            self._X = 1100
            self._Y = 0 - self.getWidth()
        if self._X == 1100 and self._Y > SCREEN_HEIGHT:
            self._X = 500
            self._Y = 0 - self.getWidth()
        self._POS = (self._X, self._Y)

    def setScale(self, SCALE_X, SCALE_Y=0):
        """resize the image based on a factor

        Args:
            SCALE_X (float): 
            SCALE_Y (float): Defaults to 0.
        """

        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
            self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth()*SCALE_X, self.getHeight()*SCALE_Y))
        