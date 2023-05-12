import pygame
from text import Text
from window import Window
from boxes import Box
from image import ImageSprite
from cannon import Cannon
from ball import Ball
from planks import Plank


##cannon moving up and down, planks marqueeing, ball shooting out of cannon in the right place


class Level1: 
    def __init__(self):
        self.__WINDOW = Window("Fat Bear")
    
        self.__TITLE = Text("Fat Bear")
        self.__TITLE.setPosition((self.__WINDOW.getWidth()//2 - self.__TITLE.getWidth()//2, 0))
        self.__TITLE.setColor((153, 255, 255))
        self.__TITLE.setFontSize(50)
        self.__BALL = Box(15, 15)
        self.__BALL.setSpeed(0)
        self.__BALL.setPosition((self.__WINDOW.getWidth()//2 - self.__BALL.getWidth()//2, 650))

        self.__BG_IMAGE = ImageSprite("images/background2.jpg")
        self.__BG_IMAGE.setScale(4)
        self.__BG_IMAGE.setPosition(
            (
                0, self.__TITLE.getHeight()
            )
        )

        self.__CANNON = Cannon("images/cannon.png")
        self.__CANNON.setScale(0.2)
        self.__CANNON.setPosition((-80, 200))
        self.__CANNON.setSpeed(15)
    

       
        self.__PLANKS = []
        for i in range(9):
            self.__PLANKS.append(Plank("images/plank.png"))
            self.__PLANKS[i].setScale(0.3)
            self.__PLANKS[i].setPosition((500, 0-300*i))

        
        self.__BALLS = []
        self.NEXT_BALL = 0
        
        

        
        

    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            KEYS_PRESSED = pygame.key.get_pressed()

            # -- PROCESSING -- #
            self.__CANNON.moveUpDown(KEYS_PRESSED)
            #self.__CANNON.checkBoundaries(-120, 800)
            
            # balls
            

            
            TIME = pygame.time.get_ticks()
            
            if KEYS_PRESSED[pygame.K_SPACE] and TIME > self.NEXT_BALL:
                DELAY = 400
                self.NEXT_BALL = TIME + DELAY
       
                BALL = Ball("images/ball.png")
                self.__BALLS.append(BALL)
                BALL.setScale(0.04)
                BALL.setPosition((self.__CANNON.getX() + 215, self.__CANNON.getY()+120))
                BALL.setSpeed(10)
                BALL.changeShoot()

            for ball in self.__BALLS:
                if ball.getShoot():
                    ball.marqueeX()
            
    
    
        
            
                   
            # planks
            for plank in self.__PLANKS:
                plank.marqueeY(self.__WINDOW.getHeight(), 6)
                    

    
            # -- OUTPUTS -- #
            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())
    
            for ball in self.__BALLS:
                self.__WINDOW.getSurface().blit(ball.getSurface(), ball.getPOS())

            for plank in self.__PLANKS:
                self.__WINDOW.getSurface().blit(plank.getSurface(), plank.getPOS())
            
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = Level1()
    GAME.run()