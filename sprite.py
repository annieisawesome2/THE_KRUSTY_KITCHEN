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
        self.__X = X
        self.__Y = Y
        self.__POS = (self.__X, self.__Y)
        self.__SPD = SPD
        self._COLOR = COLOR #white
        self.__DIR_X = 1
        self.__DIR_Y = 1
        self.LOSE = False
        

    # -- MODIFIER METHODS -- #

    #movement methods
    def isSpriteColliding(self, POSITION, DIMENSION):
        """check if a sprite is colliding with the current sprite

        Args:
            POSITION (tuple): 
            DIMENSION (tuple): 
        
        return: bool
        """
        #if BALL.isSpriteColliding(BRICK.getPOS(), BRICK.getDimensions()):
        BRICK_X = POSITION[0] #BRICK X
        BRICK_Y = POSITION[1] #BRICK Y

        BRICK_WIDTH = DIMENSION[0] # BRICK WIDTH
        BRICK_HEIGHT = DIMENSION[1] # BRICK HEIGHT

        COLLISION_STATUS = False

        if self.__X < BRICK_X + BRICK_WIDTH and self.__X + self.getWidth() > BRICK_X and self.__Y + self.__DIR_Y * self.__SPD < BRICK_Y + BRICK_HEIGHT and self.__Y + self.getHeight() + self.__DIR_Y * self.__SPD > BRICK_Y:
            self.__DIR_Y = self.__DIR_Y * -1
            COLLISION_STATUS = True

        if self.__Y < BRICK_Y + BRICK_HEIGHT and self.__Y + self.getHeight() > BRICK_Y and self.__X + self.__DIR_X * self.__SPD < BRICK_X + BRICK_WIDTH and self.__X + self.getWidth() + self.__DIR_X * self.__SPD > BRICK_X:
            self.__DIR_X = self.__DIR_X * -1
            COLLISION_STATUS = True
        
        return COLLISION_STATUS
        
    def marqueeY(self, MAX_HEIGHT, MIN_HEIGHT=0):
        self.__Y += self.__SPD
        if self.__Y > MAX_HEIGHT:
            self.setPosition((-1000,-1000))
        self.__POS = (self.__X, self.__Y)
    
    def moveAD(self, KEYS_PRESSED):
        """move sprite with WASD

        Args:
            KEYS_PRESSED (list):    
        """
        if KEYS_PRESSED[pygame.K_d]:
            self.__X += self.__SPD

        if KEYS_PRESSED[pygame.K_a]:
            self.__X -= self.__SPD
    
        self.__POS = (self.__X, self.__Y)

    def checkBoundaries(self, MAX_X, MAX_Y, MIN_X=0, MIN_Y=0):
        if self.__X > MAX_X - self.getWidth():
            self.__X = MAX_X - self.getWidth()
        if self.__X < MIN_X:
            self.__X = MIN_X 
        
        if self.__Y > MAX_Y - self.getHeight():
            self.__Y = MAX_Y - self.getHeight()
        if self.__Y < MIN_Y:
            self.__Y = MIN_Y    
        
        self.__POS = (self.__X, self.__Y)
    
    def bounceX(self, SCREEN_WIDTH_MAX, SCREEN_WIDTH_MIN=0):
        self.__X += self.__DIR_X * self.__SPD
        if self.__X > SCREEN_WIDTH_MAX - self.getWidth():
            self.__DIR_X = -1 #reverse
           

        elif self.__X < SCREEN_WIDTH_MIN:
            self.__DIR_X = 1 
            

        self.__POS = (self.__X, self.__Y)


    def bounceY(self, SCREEN_HEIGHT_MAX, SCREEN_HEIGHT_MIN=0):
        self.__Y += self.__DIR_Y * self.__SPD
        self.POS = (self.__X, self.__Y)

        if self.__Y > SCREEN_HEIGHT_MAX - self.getHeight():
            self.__POS = ((-1000, -1000)) #reverse
            self.LOSE = True
            

        elif self.__Y < SCREEN_HEIGHT_MIN:
            self.__DIR_Y = 1 
            

    
    #property methods
    def setWidth(self, WIDTH):
        self.__WIDTH = WIDTH
        self._DIM = (self.__WIDTH, self.__HEIGHT)
    
    def setHeight(self, HEIGHT):
        self.__HEIGHT = HEIGHT
        self._DIM = (self.__WIDTH, self.__HEIGHT)

    def setPosition(self, TUPLE):
        self.__X = TUPLE[0]
        self.__Y = TUPLE[1]
        self.__POS = (self.__X, self.__Y)
    
    def setColor(self, TUPLE):
        self._COLOR = TUPLE
    
    def setSpeed(self, SPD):
        self.__SPD = SPD
    
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
        return self.__POS
    
    def getSurface(self):
        return self._SURFACE
    
    def getColor(self):
        return self._COLOR

    

    

    