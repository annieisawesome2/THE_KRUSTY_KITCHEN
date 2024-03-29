from sprite import MySprite
import pygame

class Items(MySprite):

    def __init__(self, IMAGE_FILE):
        MySprite.__init__(self)
        self.__FILE_LOC = IMAGE_FILE  ## ENCAPSULATION (protecting and hiding data through an interface)
        self._SURFACE = pygame.image.load(self.__FILE_LOC).convert_alpha()
        self.__COLLECTED = False
        self.GO = False # self.GO
        self.SPEED = 0

    # -- MODIFIER METHODS -- #
    def setGo(self, STATUS):
        self.GO = STATUS
    
    def setCollected(self, STATUS):
        self.__COLLECTED = STATUS

    def setSpeed(self, NUMBER):
        self.SPEED = NUMBER

    def setDirX(self, DIRECTION):
        self._DIR_X = DIRECTION
        self._POS = (self._X*self._DIR_X, self._Y)

    def scaleBurgerItems(self):
        ITEM_NAME = self.getFileLoc()
        if ITEM_NAME == "images/spatula.png":
            self.setScale(0.4)
        elif ITEM_NAME == "images/bun_bottom.png":
            self.setScale(1.2, 1)
        elif ITEM_NAME == "images/cheese.png":
            self.setScale(1.4, 1.2)
        elif ITEM_NAME == "images/lettuce.png":
            self.setScale(0.6)
        elif ITEM_NAME == "images/pickles.png":
            self.setScale(0.18, 0.2)
        elif ITEM_NAME == "images/tomatos.png":
            self.setScale(1.7, 1.2)
        elif ITEM_NAME == "images/onions.png":
            self.setScale(1.5)
        elif ITEM_NAME == "images/ketchup.png" or ITEM_NAME == "images/mustard.png":
            self.setScale(0.2, 0.15)
        else:
            self.setScale(1.2)
        
    # movement methods
    def marqueeY(self, SCREEN_HEIGHT, SPEED):
        """
        Moves object in a vertical snake pattern.
        """
        self.SPEED = SPEED
        self._Y += self.SPEED*self._DIR_Y
        if self._X == 550 and self._Y > SCREEN_HEIGHT+100:
            self._X = 850
            self._Y = SCREEN_HEIGHT
            self._DIR_Y = -1

        if self._X == 850 and self._Y < -100 - self.getHeight():
            self._X = 1100
            self._Y = 0 - self.getWidth()
            self._DIR_Y = 1
            
        self._POS = (self._X, self._Y)
    
    def marqueeX(self, SCREEN_WIDTH, SPEED):
        """
        Moves object in a horizontal snake pattern.
        """
        self.SPEED = SPEED
        self._X += self.SPEED*self._DIR_X
        if self._Y == 50 and self._X > SCREEN_WIDTH:
            self._Y = 250
            self._X = SCREEN_WIDTH
            self._DIR_X = -1

        if self._Y == 250 and self._X < 0 - self.getWidth():
            self._Y = 470
            self._X = 0 - self.getHeight()
            self._DIR_X = 1
            
        if self._Y == 470 and self._X > SCREEN_WIDTH: #SCREEN_HEIGHT
            self.setPosition((-1000, -1000))
            
        self._POS = (self._X, self._Y)
    
    def moveX(self, MAX_WIDTH):
        self._X += 20
        if self._X > MAX_WIDTH:
            self.setPosition((-1000,-1000))
        self._POS = (self._X, self._Y)

    # -- ACCESSOR METHODS -- #
    def getGo(self):
        return self.GO

    def getCollected(self):
        return self.__COLLECTED

    def getFileLoc(self):
        return self.__FILE_LOC