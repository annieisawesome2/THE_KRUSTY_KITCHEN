import pygame

from sprite import MySprite
from window import Window

class Box(MySprite):
    ##Box object inheriting from MySprite
    def __init__(self, WIDTH=1, HEIGHT=1):
        MySprite.__init__(self, WIDTH, HEIGHT)
        self._SURFACE = pygame.Surface(self._DIM, pygame.SRCALPHA, 32) ## rerender the surface
        self._SURFACE.fill(self._COLOR)
        self.POWER = False

        ## ENCAPSULATION (protecting and hiding data through an interface)
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT
        self.HEALTH = 0

    def setHealth(self):
        """setting health for bubble
        """
        self.HEALTH -= 1
    
    def setColor(self, TUPLE):
        #polymorphs the setColor class from MySprite
        MySprite.setColor(self, TUPLE)
        self._SURFACE.fill(self._COLOR)

    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
    
    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def getColor(self):
        return self._COLOR





 





