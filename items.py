from sprite import MySprite
import pygame

class Items(MySprite):

    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__COLLECTED = False
        self.GO = False
    
    def setGo(self, STATUS):
        self.GO = STATUS
    
    def getGo(self):
        return self.GO

    # -- MODIFIER METHODS -- #
    def setValue(self, VALUE):
        self.__VALUE = VALUE
    
    def setCollected(self, STATUS):
        self.__COLLECTED = STATUS

    def setDirX(self, DIRECTION):
        self._DIR_X = DIRECTION
        self._POS = (self._X*self._DIR_X, self._Y)

    # -- ACCESSOR METHODS -- #
    def getCollected(self):
        return self.__COLLECTED

    def getFileLoc(self):
        return self.__FILE_LOC

    def marqueeY(self, SCREEN_HEIGHT, SPEED):
        """
        Moves object in a vertical snake pattern.
        """
        self._Y += SPEED*self._DIR_Y
        if self._X == 550 and self._Y > SCREEN_HEIGHT+100:
            self._X = 850
            self._DIR_Y = -1

        if self._X == 850 and self._Y < -100 - self.getHeight():
            self._X = 1100
            self._DIR_Y = 1
            
        # if self._X == 1100 and self._Y > 600:
        #     self.setPosition((-1000, -1000))
            
        self._POS = (self._X, self._Y)
    
    def marqueeX(self, SCREEN_WIDTH, SPEED):
        """
        Moves object in a vertical snake pattern.
        """
        #if self._Y == 50 and self._X < SCREEN_WIDTH:
        self._X += SPEED*self._DIR_X
        if self._Y == 50 and self._X > SCREEN_WIDTH:
            self._Y = 200
            self._DIR_X = -1

        if self._Y == 200 and self._X < 0 - self.getWidth():
            self._Y = 350
            self._DIR_X = 1
            
        if self._Y == 350 and self._X > SCREEN_WIDTH: #SCREEN_HEIGHT
            self.setCollected(True)
            self.setPosition((-1000, -1000))
            
        self._POS = (self._X, self._Y)
    
    
  