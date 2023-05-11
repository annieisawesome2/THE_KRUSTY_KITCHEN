from sprite import MySprite
import pygame


class Ball(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()

    def setScale(self, SCALE_X, SCALE_Y=0):
        """resize the image based on a factor

        Args:
            SCALE_X (float): 
            SCALE_Y (float): Defaults to 0.
        """

        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
            self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth()*SCALE_X, self.getHeight()*SCALE_Y))

    def marqueeX(self):
        self._X += self._SPD
        self._POS = (self._X, self._Y)