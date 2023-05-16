from sprite import MySprite
import pygame

class Items(MySprite):

    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__VALUE = 0
        self.__PRESENCE = False
        self.__EATEN = False

    # -- MODIFIER METHODS -- #
    def setPosition(self, PLANK_POS):
        MySprite.setPosition(self, PLANK_POS)
        self._POS = (PLANK_POS[0], PLANK_POS[1] - self.getHeight())

    def setValue(self, VALUE):
        self.__VALUE = VALUE
        
    def setPresence(self):
        if not (self.getPOS()[0] == 500 and self.getPOS()[1] < 0):
            self.__PRESENCE = True
        else:
            self.__PRESENCE = False
    
    def setEaten(self, STATUS):
        self.__EATEN = STATUS

    # -- ACCESSOR METHODS -- #
    def getValue(self):
        return self.__VALUE

    def getPresence(self):
        return self.__PRESENCE

    def getEaten(self):
        return self.__EATEN