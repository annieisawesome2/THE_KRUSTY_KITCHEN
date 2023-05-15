from sprite import MySprite
import pygame


class Fruits(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__VALUE = 0

    def setPosition(self, PLANK):
        MySprite.setPosition(self, PLANK)
        self._POS = (PLANK.getPosition()[0], PLANK.getPosition()[1] - self.getHeight())

    def setValue(self, VALUE):
        self.__VALUE = VALUE
    
    def getValue(self):
        return self.__VALUE