from sprite import MySprite
from ball import Ball
import pygame

class Cannon(MySprite):
    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        
    def moveUpDown(self, KEYS_PRESSED):
        """move cannon up and down

        Args:
            KEYS_PRESSED (list):    
        """
        
        if KEYS_PRESSED[pygame.K_UP]:
            self._Y -= self._SPD

        if KEYS_PRESSED[pygame.K_DOWN]:
            self._Y += self._SPD
    
        self._POS = (self._X, self._Y)




