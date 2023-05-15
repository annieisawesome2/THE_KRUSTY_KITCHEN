from sprite import MySprite
import pygame


class Ball(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.SHOOT = False
    
    def changeShoot(self):
        self.SHOOT = True

    def getShoot(self):
        return self.SHOOT

    def marqueeX(self):
        self._X += self._SPD
        self._POS = (self._X, self._Y)