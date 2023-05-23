import pygame

class MySprite:
    """many of the common attributes and methods for sprites in pygame
    """
    def __init__(self, HEIGHT=0, WIDTH=0, X=0, Y=0, SPD=0, COLOR = (255, 255, 255)):
        ## ABSTRACTION (setting appropiate level of complexity and detail to what game requires sprite to be)
        self.__HEIGHT = HEIGHT ## ENCAPSULATION (protecting and hiding data through an interface)
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
        self._SURFACE = pygame.Surface
        self._X = X
        self._Y = Y
        self._POS = (self._X, self._Y)
        self._SPD = SPD
        self._COLOR = COLOR #white
        self._DIR_X = 1
        self._DIR_Y = 1
        self.LOSE = False
        

    # -- MODIFIER METHODS -- #

    #movement methods
    def isSpriteColliding(self, POSITION, DIMENSION):
        """check if a sprite is colliding with the current sprite

        Args:
            POSITION (tuple): 
            DIMENSION (tuple): 
        returns:
            bool
        """
        SPRITE_X = POSITION[0]

        SPRITE_W = DIMENSION[0]
     
        if SPRITE_X >= self._X - SPRITE_W and SPRITE_X <= self._X + self.getWidth():
            
            return True
        
        return False

    def marqueeY(self, MAX_HEIGHT, MIN_HEIGHT=0):
        self._Y += self._SPD
        if self._Y > MAX_HEIGHT:
            self.setPosition((-1000,-1000))
        self._POS = (self._X, self._Y)
    
    def moveAD(self, KEYS_PRESSED):
        """move sprite with WASD

        Args:
            KEYS_PRESSED (list):    
        """
        if KEYS_PRESSED[pygame.K_d]:
            self._X += self._SPD

        if KEYS_PRESSED[pygame.K_a]:
            self._X -= self._SPD
    
        self._POS = (self._X, self._Y)

    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X=-50, MIN_Y= -20):
        if self._X > MAX_X - self.getWidth():
            self._X = MAX_X - self.getWidth()
        if self._X < MIN_X:
            self._X = MIN_X 
        
        if self._Y > MAX_Y - self.getHeight():
            self._Y = MAX_Y - self.getHeight()
        if self._Y < MIN_Y:
            self._Y = MIN_Y    
        
        self._POS = (self._X, self._Y)
    
    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        self._X += self.__DIR_X * self._SPD
        if self._X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__DIR_X = -1 #reverse
           

        elif self._X < SCREEN_WIDTH_MIN:
            self.__DIR_X = 1 
            

        self._POS = (self._X, self._Y)


    def bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        self._Y += self.__DIR_Y * self._SPD
        self.POS = (self._X, self._Y)

        if self._Y > SCREEN_HEIGHT_MAX - self.getHeight():
            self._POS = ((-1000, -1000)) #reverse
            self.LOSE = True
            

        elif self._Y < SCREEN_HEIGHT_MIN:
            self.__DIR_Y = 1 
            

    
    #property methods
    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
    
    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setScale(self, SCALE_X, SCALE_Y=0):
        """resize the image based on a factor

        Args:
            SCALE_X (float): 
            SCALE_Y (float): Defaults to 0.
        """

        if SCALE_Y == 0:
            SCALE_Y = SCALE_X
            self._SURFACE = pygame.transform.scale(self._SURFACE, (self.getWidth()*SCALE_X, self.getHeight()*SCALE_Y))

    def setPosition(self, TUPLE):
        self._X = TUPLE[0]
        self._Y = TUPLE[1]
        self._POS = (self._X, self._Y)
    
    def setColor(self, TUPLE):
        self._COLOR = TUPLE
    
    def setSpeed(self, SPD):
        self._SPD = SPD
    
    def setDimensions(self, TUPLE):
        self.__WIDTH = TUPLE[0]
        self.__HEIGHT = TUPLE[1]
        self._DIM = (self.__WIDTH, self.__HEIGHT)
    


    
    # -- ACCESSOR METHODS -- #
    def getWidth(self):
        return self._SURFACE.get_width()
    
    def getHeight(self):
        return self._SURFACE.get_height()

    def getDimensions(self):
        return (self._SURFACE.get_width(), self._SURFACE.get_height())
    
    def getPOS(self):
        return self._POS
    
    def getX(self):
        return self._X
    
    def getY(self):
        return self._Y
    
    def getSurface(self):
        return self._SURFACE
    
    def getColor(self):
        return self._COLOR

    

    

    