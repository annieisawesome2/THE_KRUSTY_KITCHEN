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



if __name__ == "__main__":
    pygame.init()
    
    WINDOW = Window("Box Test")
    BALL = Box(50, 50)
    BALL.setSpeed(10)
    BALL.setColor((0, 0, 255))
    BRICK = Box(100, 150)
    BRICK.setPosition((300, 300))
    BRICK2 = Box(100, 150)
    BRICK2.setPosition((800, 200))
    BALL.setPosition((10, 50))

    while True:
        # -- INPUTS -- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        PRESSED_KEYS = pygame.key.get_pressed()

        # -- PROCESSING -- #
        #BOX.marqueeX(WINDOW.getWidth())
        BALL.bounceX(WINDOW.getWidth())
        BALL.bounceY(WINDOW.getHeight())
        BALL.checkBoundaries(WINDOW.getWidth(), WINDOW.getHeight())


        if BALL.isSpriteColliding(BRICK.getPOS(), BRICK.getDimensions()):
            BRICK.setColor((0, 255, 255))
        else:
            BRICK.setColor((255, 255, 255))

        if BALL.isSpriteColliding(BRICK2.getPOS(), BRICK2.getDimensions()):
            BRICK2.setColor((0, 255, 255))
        else:
            BRICK2.setColor((255, 255, 255))


        # -- OUTPUTS -- #
        WINDOW.clearScreen()
        WINDOW.getSurface().blit(BALL.getSurface(), BALL.getPOS())
        WINDOW.getSurface().blit(BRICK.getSurface(), BRICK.getPOS())
        WINDOW.getSurface().blit(BRICK2.getSurface(), BRICK2.getPOS())
        WINDOW.updateFrame()


 





