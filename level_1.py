import pygame
from text import Text
from window import Window
from boxes import Box
from image import ImageSprite
from cannon import Cannon
from ball import Ball


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
        

        self.__BALLS = []
        for i in range(1000):
            self.__BALLS.append(Ball("images/ball.png"))

        for ball in self.__BALLS:
            ball.setScale(0.04)
            ball.setPosition((-1000, -1000))
            ball.setSpeed(25)


    



        self.__PLANK = ImageSprite("images/plank.png")
        self.__PLANK.setScale(0.3)
        self.__PLANK.setPosition((900, 100))
     



    def run(self):
        while True:
            # -- INPUTS -- #
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            KEYS_PRESSED = pygame.key.get_pressed()

            self.__CANNON.moveUpDown(KEYS_PRESSED)
            #self.__CANNON.checkBoundaries(-120, 800)

            if KEYS_PRESSED[pygame.K_SPACE]:
                self.__BALL.setPosition((self.__CANNON.getX()+215, self.__CANNON.getY()+120))
                self.__BALL.changeShoot()
            
            if self.__BALL.getShoot():
                self.__BALL.marqueeX()


            self.__WINDOW.clearScreen()
            self.__WINDOW.getSurface().blit(self.__BG_IMAGE.getSurface(), self.__BG_IMAGE.getPOS())
            self.__WINDOW.getSurface().blit(self.__CANNON.getSurface(), self.__CANNON.getPOS())
            self.__WINDOW.getSurface().blit(self.__BALL.getSurface(), self.__BALL.getPOS())
            self.__WINDOW.getSurface().blit(self.__PLANK.getSurface(), self.__PLANK.getPOS())
            self.__WINDOW.getSurface().blit(self.__TITLE.getSurface(), self.__TITLE.getPOS())
            self.__WINDOW.updateFrame()


if __name__ == "__main__":
    pygame.init()
    GAME = Level1()
    GAME.run()