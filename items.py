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
        self.go = False
    
    def setgo(self):
        self.go = True
    
    def getGo(self):
        return self.go

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
            
        if self._X == 1100 and self._Y > 500: #SCREEN_HEIGHT
            self.setPosition((-1000, -1000))
            
        self._POS = (self._X, self._Y)
  